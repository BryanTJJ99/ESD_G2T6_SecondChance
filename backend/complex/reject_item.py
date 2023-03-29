# Flask imports
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# OS and error imports
import os, sys

# HTTP imports
import requests
from invokes import invoke_http

import amqp_setup # compose version
import pika
import json
from slack_sdk import WebClient

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# slack_client = WebClient(token='supposed to put api token here')
# response = slack_client.chat_postMessage(
#             channel='#general',
#             text='Hello, world!'
#         ) 
# idk how to view the channel and verify also 

department_url = 'http://localhost:8080/department'
carbon_calculator_url = 'http://localhost:5002/carbon_calc'
create_item_url = 'http://localhost:5000/create'
item_url = 'http://localhost:5000/item'

@app.route("/reject_item/<string:item_id>", methods=["POST"])
@cross_origin()
def reject_item(item_id):
    try:
        return process_reject_item(item_id)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ex_str = f"{str(e)} at {str(exc_type)}: {fname}: line {str(exc_tb.tb_lineno)}"
        print(ex_str)

        return jsonify({
            "code": 500,
            "message": f"reject_item.py internal error: {ex_str}"
        })
    
def process_reject_item(item_id):

    # item microservice 
    old_item_result =  invoke_http(
        f"{item_url}/{item_id}",
        method="GET"
    )

    # item retrieval fail
    if old_item_result['code'] not in range(200,300):

        print('\n\n-----Publishing item retrieval error message with routing_key=retrieval.error-----')
        message = {
            "code": 404,
            "message_type": "retrieval_error",
            "data": old_item_result,
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="retrieval.error", 
        body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
    
        print("\nItem retrieval error published to RabbitMQ Exchange.\n")

        return old_item_result


    #  item retrieval successful

    print('\n\n-----Publishing the i†em retrieval notification message with routing_key=retrieval.notify-----')

    old_item_data = old_item_result['data']

    message = {
        "code": 201,
        "message_type": "retrieval_notification",
        "data": old_item_data
    }

    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="retrieval.notify", 
    body=message, properties=pika.BasicProperties(delivery_mode = 2))

    print("\nItem retrieval notification published to RabbitMQ Exchange.\n")

    # delete request but would this delete the item altogether
    if old_item_data["status"] == "pending":
        item_delete_result = invoke_http(
        f"{item_url}/{old_item_data['item_id']}",
        method="DELETE"
    )

        if item_delete_result["code"] not in range(200,300):
                # request deletion fail

            print('\n\n-----Publishing the item deletion error message with routing_key=item_rejection.error-----')        

            message = {
                "code": 400,
                "message_type": "item_deletion_error",
                "data": item_delete_result["message"]
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="item_rejection.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

            print("\nItem rejection error published to RabbitMQ Exchange.\n")
            return item_delete_result

        item_delete_data = item_delete_result["data"]


        # rejection successful

        print('\n\n-----Publishing the item deletion notification message with routing_key=item_rejection.notify-----')        

        message = {
            "code": 201,
            "message_type": "item_deletion_notification",
            "data": item_delete_data
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="item_rejection.notify", 
        body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

        print("\nItem deletion notification published to RabbitMQ Exchange.\n")

        item_status = {
            "status": "rejected"
        }
        new_item_result = invoke_http(
            f"{item_url}/{item_id}",
            method="PUT",
            json=item_status
        )

        if new_item_result["code"] not in range(200,300):

            print('\n\n-----Publishing the item rejection update error message with routing_key=reject.error-----')        

            message = {
                    "code": 400,
                    "message_type": "reject_error",
                    "data": new_item_result
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="reject.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

            print("\nItem rejection update error published to RabbitMQ Exchange.\n")

            return new_item_result

        new_item_data = new_item_result["data"]

        # item rejection success

        print('\n\n-----Publishing the item rejection notification message with routing_key=reject.notify-----')       


        message = {
            "code": 201,
            "message_type": "reject_notification",
            "data": new_item_data
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="reject.notify", 
        body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

        print("\nItem rejection notification published to RabbitMQ Exchange.\n")

        return new_item_result


# item rejection status error

    print('\n\n-----Publishing the item rejection status error message with routing_key=reject_status.error-----')        

    message = {
        "code": 403,
        "message_type": "reject_status_error",
        "data": old_item_data
    }
    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="reject_status.error", 
    body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

    print("\nItem rejection status error published to RabbitMQ Exchange.\n")

    # ##################### END OF AMQP code

    return jsonify({
        "code": 403,
        "message": f"Unable to reject item. Item status is already {old_item_data['status']}."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5102, debug=True)
    
