from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import os, sys

import requests
from invokes import invoke_http

from os import environ

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

department_url = environ.get('department_URL') or 'http://localhost:8080/department'
item_url = environ.get('item_URL') or 'http://localhost:5000'

@app.route("/accept_item", methods=['GET'])
@cross_origin()
def accept_item():
    try:
        item_id = request.args.get('itemId')
        accepted_department_id = request.args.get('departmentId')
        result = process_accept_item(accepted_department_id, item_id)
        return result
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ex_str = f"{str(e)} at {str(exc_type)}: {fname}: line {str(exc_tb.tb_lineno)}"
        print(ex_str)
    
        return jsonify({
            "code": 500,
            "message": f"accept_item.py internal error: {ex_str}" 
        })

def process_accept_item(accepted_department_id, item_id):
    amqp_setup.check_setup()
    # get accepted department data
    department_result = invoke_http(
        f"{department_url}/{accepted_department_id}",
        method='GET'
    )

    if department_result["code"] not in range(200, 300):
        print('\n\n-----Publishing the (department error) message with routing_key=department.error-----')
        code = department_result['code']
        message = {
            "code": 400,
            "message_type": "department_error",
            "data": "Invalid department ID"
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(code))
        return department_result
    
    # if department exists
    department_data = department_result['data']
    message = {
        "code": 201,
        "message_type": 'department_get_request',
        "data": department_data
    }

    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))

    # get item data
    item_result = invoke_http(
        f'{item_url}/{item_id}',
        method='GET'
    )

    # if item does not exist
    if item_result["code"] not in range(200, 300):
        print('\n\n-----Publishing the (item error) message with routing_key=item.error-----')
        code = item_result['code']
        message = {
            "code": 400,
            "message_type": "item_error",
            "data": "Invalid item ID"
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='item.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nItem error - Code {} - published to the RabbitMQ Exchange:".format(code))
        return item_result

    # if item exists
    item_data = item_result['data']
    buyerIds = item_data['buyerIds']
    original_departmentId = item_data['departmentId']
    # item's carbon emission
    item_carbon_emissions_saved = item_data['carbonEmission']

    # check if accepted_department id in buyerIds
    if accepted_department_id not in buyerIds:
        print('\n\n-----Publishing the (item error) message with routing_key=item.error-----')
        message = {
            "code": 400,
            "message_type": "item_error",
            "data": "Invalid buyer ID"
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='item.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nItem error - Code {} - published to the RabbitMQ Exchange:".format(400))
        return item_result
    
    # clear buyerIds
    item_data['buyerIds'] = []
    # remove listing
    item_data['isListed'] = False
    # change department id item belongs to
    item_data['departmentId'] = accepted_department_id
    # change company id item belongs to
    item_data['companyId'] = department_data['companyId']

    item_id = item_data['_id']['$oid']
    item_data.pop('_id')
    # edit item
    edited_item_result = invoke_http(
        f'{item_url}/edit/{item_id}',
        method='PUT',
        json=item_data
    )

    # if edit item fails
    if edited_item_result["code"] not in range(200, 300):
        print('\n\n-----Publishing the (item error) message with routing_key=item.error-----')
        code = edited_item_result['code']
        message = {
            "code": 400,
            "message_type": "edit_item_error",
            "data": "Edit Item error"
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='item.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nItem error - Code {} - published to the RabbitMQ Exchange:".format(code))
        return item_result
    
    # if edit item works
    item_data = item_result['data']
    message = {
        "code": 201,
        "message_type": 'item_edit_request',
        "data": item_data
    }

    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='item.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))

    # remove itemId from original department
    deleteItemId_result = invoke_http(
        f'{department_url}/deleteItemID/{original_departmentId}/{item_id}',
        method='DELETE'
    )

    # if remove itemId does not work
    if deleteItemId_result["code"] not in range(200, 300):
        print('\n\n-----Publishing the (department error) message with routing_key=department.error-----')
        code = deleteItemId_result['code']
        message = {
            "code": 400,
            "message_type": "edit_item_error",
            "data": "Edit Item error"
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(code))
        return deleteItemId_result
    
    # if remove itemId works
    deleteItemId_data = deleteItemId_result['data']
    message = {
        "code": 201,
        "message_type": 'department_delete_item_id_request_error',
        "data": deleteItemId_data
    }

    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))

    # add itemId to itemId array in new department
    addItemId_result = invoke_http(
        f'{department_url}/addItemID/{accepted_department_id}/{item_id}',
        method='POST',
        json=item_data
    )

    # if addItemId does not work
    addItemId_data = addItemId_result['data']
    if addItemId_result["code"] not in range(200, 300):
        print('\n\n-----Publishing the (department error) message with routing_key=department.error-----')
        code = addItemId_result['code']
        message = {
            "code": 400,
            "message_type": "department_add_item_id_request_error",
            "data": addItemId_data
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(code))
        return item_result

    # if addItemId works
    message = {
        "code": 201,
        "message_type": 'department_delete_item_id_request_error',
        "data": deleteItemId_data
    }

    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))

    # add carbon amount to new department
    addDepartmentCarbon_result = invoke_http(
        f'{department_url}/addDepartmentCarbon/{accepted_department_id}/{item_carbon_emissions_saved}',
        method='PUT'
    )

     # if addDepartmentCarbon does not work
    addDepartmentCarbon_data = addDepartmentCarbon_result['data']
    if addDepartmentCarbon_result["code"] not in range(200, 300):
        print('\n\n-----Publishing the (department error) message with routing_key=department.error-----')
        code = addItemId_result['code']
        message = {
            "code": 400,
            "message_type": "department_add_carbon_request_error",
            "data": addDepartmentCarbon_data
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(code))
        return addDepartmentCarbon_result

    # if addDepartmentCarbon works
    message = {
        "code": 201,
        "message_type": 'department_delete_item_id_request_error',
        "data": addDepartmentCarbon_data
    }

    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
    
    #---------------------------------------------------------------------------------
    #slack notification for accepted buyer
    # buyer_slack_item = {"item_id": item_id, "item_name": item_data["itemName"], "buyer_id": accepted_department_id, "isAccept":True}

    # buyer_slack_result = invoke_http(
    #     f"{slack_url}",
    #     method="POST",
    #     json=buyer_slack_item
    # )

    # print(buyer_slack_result)
        
        
    # if buyer_slack_result['code'] not in range(200, 300):
    #     print('\n\n-----Publishing the (slack error) message with routing_key=slack.error-----')
                
    #     message = {
    #         "code": 400,
    #         "message_type": "business_error",
    #         "data": "Invalid slack response"
    #     }
    #     message = json.dumps(message)
    #     amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='slack.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
    #     print("\nSlack error - Code {} - published to the RabbitMQ Exchange:".format(buyer_slack_result['code']))
    #     return buyer_slack_result
        
    # else:
    #     message = {
    #         "code": 201,
    #             "message_type": 'slack_notification',
    #             "data": buyer_slack_result['data']
    #     }
    #     message = json.dumps(message)
    #     amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='slack.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
    #     print("------------ SLACK NOTIFICATION SENT SUCCESSFULLY - {} ------------".format(buyer_slack_result['data']))

    # ##################### END OF AMQP code

    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3101, debug=True)



