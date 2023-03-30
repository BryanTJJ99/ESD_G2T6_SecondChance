# Flask imports
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# OS and error imports
import os, sys
from os import environ

# HTTP imports
import requests
from invokes import invoke_http

# # # AMQP imports
## switch the comments for the amqp path to test locally with (python <filename>.py)
# from amqp import amqp_setup # local path
import amqp_setup # compose version
import pika
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

department_url = 'http://localhost:8080/department'
item_url = 'http://localhost:5000'
slack_url = 'http://localhost:5008/slack'

@app.route("/reject_item", methods=["POST"])
@cross_origin()
def reject_item():
    try:
        itemId = request.args.get('itemId')
        rejectedDepartmentId = request.args.get('departmentId')

        return process_reject_item(itemId, rejectedDepartmentId)
    
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ex_str = f"{str(e)} at {str(exc_type)}: {fname}: line {str(exc_tb.tb_lineno)}"
        print(ex_str)

        return jsonify({
            "code": 500,
            "message": f"reject_item.py internal error: {ex_str}"
        })
    
def process_reject_item(itemId, rejectedDepartmentId):
    #------------------------------------------------------------------------------
    #get data from department
    department_result = invoke_http(
        f"{department_url}/{rejectedDepartmentId}",
        method="GET",
    )
    
    print('error1')
    if department_result['code'] not in range(200,300):
        print('\n\n-----Publishing the message with routing_key=department.error-----')

        message = {
            "code": 400,
            "message_type": "department_error",
            "data": department_result
        }

        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(department_result['code']))
        return department_result['data']
    else:
        message = {
            "code": 201,
            "message_type": 'department_put_request',
            "data": department_result['data']
        }
        print('error3')
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("------------ DEPARTMENT RETRIEVED SUCCESSFULLY - {} ------------".format(department_result['data']))

#------------------------------------------------------------------------------
#get data from item

    item_result = invoke_http(
        f"{item_url}/{itemId}",
        method="GET",
    )
    
    item_data = item_result["data"]
    if item_result['code'] not in range(200,300):
        print('\n\n-----Publishing the message with routing_key=item.error-----')

        message = {
            "code": 400,
            "message_type": "item error",
            "data": item_result['data']
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='item.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\item error - Code {} - published to the RabbitMQ Exchange:".format(item_result['code']))
        return item_result
    else:
        message = {
            "code": 201,
            "message_type": 'item get request',
            "data": item_result['data']
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='item.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("------------ ITEM RETRIEVED SUCCESSFULLY - {} ------------".format(item_data))

    #------------------------------------------------------------------------------
    #slack notification for rejected list

    rejected_slack_item = {"itemId": itemId, "itemName": item_data["itemName"], "buyerId": rejectedDepartmentId, "isAccept":False}

    rejected_slack_result = invoke_http(
            f"{slack_url}",
            method="POST",
            json=rejected_slack_item
        )

    if rejected_slack_result['code'] not in range(200, 300):
        print('\n\n-----Publishing the (slack error) message with routing_key=slack.error-----')
        
        message = {
            "code": 400,
            "message_type": "Invalid slack response",
            "data": rejected_slack_result['data']
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='slack.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nSlack error - Code {} - published to the RabbitMQ Exchange:".format(rejected_slack_result['code']))
        return rejected_slack_result
    
    else:
        message = {
            "code": 201,
                "message_type": 'slack_notification',
                "data": rejected_slack_result['data']
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='slack.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("------------ SLACK NOTIFICATION SENT SUCCESSFULLY - {} ------------".format(rejected_slack_result['data']))

    return "success"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5102, debug=True)