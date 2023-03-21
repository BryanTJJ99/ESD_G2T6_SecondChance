from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import os, sys

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

department_url = 'http://localhost:5004/department'
carbon_calculator_url = 'http://localhost:5005/carbon_calc'
create_item_url = 'http://localhost:5006/create'
item_url = 'http://localhost:5007/item'

@app.route("/accept_item/<string:item_id>", methods=["POST"])
@cross_origin
def accept_item(item_id):
    if request.is_json:
        try:
            result = process_accept_item(item_id)
            return result 

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = f"{str(e)} at {str(exc_type)}: {fname}: line {str(exc_tb.tb_lineno)}"
            print(ex_str) 

            return jsonify ({
                "code": 500,
                "message": f"accept_item.py internal error: {ex_str}"
            })


def process_accept_item(item_id):
    # retrieving item 
    item = request.get_json()
    old_item_result = invoke_http(
        f"{item_url}/{item_id}",
        method="GET"
    )

    # if item retrieval fails
    if old_item_result["code"] not in range(200,300):
    
        print('\n\n-----Publishing the item retrieval error message with routing_key=retrieval.error-----')  

        message = {
            "code": 404,
            "message_type": "retrieval_error",
            "data": old_item_result,
        }

        message = json.dumps(message) 

        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="retrieval.error", 
        body=message, properties=pika.BasicProperties(delivery_mode = 2)) 


        print("\nitem retrieval error published to RabbitMQ Exchange.\n")
        return old_item_result
    
    # else item retrieval successful 
    old_item_data = old_item_result['data']

    print('\n\n-----Publishing the item retrieval notification message with routing_key=retrieval.notify-----')        

    message = json.dumps({
        "code": 201,
        "message_type": "retrieval_notification",
        "data": old_item_data
    })

    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="retrieval.notify", 
    body=message, properties=pika.BasicProperties(delivery_mode = 2))

    print("\nItem retrieval notification published to RabbitMQ Exchange.\n")


    # item acceptance successful
    if old_item_data["status"] == False:
        item_status = {
            "status": True
        }
        new_item_result = invoke_http(
            f"{item_url}/{item_id}",
            method="PUT",
            json=item_status
        )   

        print('\n\n-----Publishing the item accept notification message with routing_key=accept.notify-----')        

        new_item_data = new_item_result["data"]

        message = {
            "code": 201,
            "message_type": "accept_notification",
            "data": new_item_data
        }

        message = json.dumps(message)

        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="accept.notify", 
        body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
    
        print("\nItem accept notification published to RabbitMQ Exchange.\n")

        # add carbon to department's overall carbon saved
        amqp_setup.check_setup()
        # get department of item created
        department_result = invoke_http(
            f"{department_url}/{item['creatorId']}",
            method="GET"
        )

        # if department does not exist
        if department_result["code"] not in range(200, 300):
            print('\n\n-----Publishing the (department error) message with routing_key=department.error-----')
            code = department_result['code']
            message = {
                "code": 400,
                "message_type": "business_error",
                "data": "Invalid department ID"
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(code))
            return department_result
        
        # department does exist so post item
        department_data = department_result['data']
        item_result = invoke_http(
        f"{create_item_url}",
        method='POST',
        json=item
        )

        item_data = item_result['data']
        # store new item_id in department
        item_id = item_data['_id']
        department_items = department_data['items']
        department_items.append(item_id)
        department_data['items'] = department_items
        # add carbon data to department
        department_carbon = department_data['totalCarbon']
        department_data['totalCarbon'] = department_carbon + item['carbonEmission']
        # run department put request
        department_update_result = invoke_http(
            f"{department_url}/edit/{item['creatorId']}",
            method='PUT',
            json=department_data
        )
        
        department_update_data = department_update_result['data']

        # department not updated
        if department_update_result['code'] not in range(200,300):
            code = department_update_result['code']
            print('\n\n-----Publishing the (department error) message with routing_key=department.error-----')
            message = {
                "code": 400,
                "message_type": "department_error",
                "data": department_update_data
            }

            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(code))
            return department_update_result
        
        # department updated
        else:
            message = {
                "code": 201,
                "message_type": 'department_put_request',
                "data": department_update_data
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("------------ DEPARTMENT EDITED SUCCESSFULLY - {} ------------".format(department_update_result))
            return department_update_result


    # handle error -> not accepted
    print('\n\n-----Publishing the item accept update message with routing_key=accept.error-----')        

    message = json.dumps({
        "code": 400,
        "message_type": "accept_error",
        "data": old_item_data
    })
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="accept.error", 
    body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

    print("\nItem accept error published to RabbitMQ Exchange.\n")

    # ##################### END OF AMQP code

    return jsonify({
        "code": 403,
        "message": f"Unable to accept item. Item status is already {old_item_data['status']}."
    })

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5101, debug=True)

