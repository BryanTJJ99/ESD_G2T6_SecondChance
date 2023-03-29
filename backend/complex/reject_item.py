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

department_url = 'http://localhost:5004/department'
carbon_calculator_url = 'http://localhost:5005/carbon_calc'
create_item_url = 'http://localhost:5006/create'
item_url = 'http://localhost:5007/item'
slack_url = 'http://localhost:5008/slack'

@app.route("/reject_item", methods=["POST"])
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
    
def process_reject_item(request):
    item = request["item"]
    rejectedId = request["rejectedId"]

    #-----------------------------------------------------------
    # update list of offers by removing rejectedId
    buyer_list = item["buyerId"]
    buyer_list.pop(rejectedId)

    updated_item = {
        "_id": item['_id'],
        "itemName": item['itemName'],
        "itemCategory": item["itemCategory"],
        "isListed": True,
        "itemPicture": item["itemPicture"],
        "itemDescription": item["itemDescription"],
        "carbonEmission": item["carbonEmission"],
        "buyerId": buyer_list,
        "companyId": item["companyId"],
        "departmentId": item["departmentId"]
    }
    
    remove_reject_result =  invoke_http(
        f"{item_url}/{item['_id']}",
        method="PUT",
        json=updated_item
    )

    if remove_reject_result['code'] not in range(200,300):

        print('\n\n-----Publishing item retrieval error message with routing_key=retrieval.error-----')
        message = {
            "code": 404,
            "message_type": "retrieval_error",
            "data": remove_reject_result,
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="retrieval.error", 
        body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
    
        print("\nItem retrieval error published to RabbitMQ Exchange.\n")

        return remove_reject_result


    print('\n\n-----Publishing the i†em retrieval notification message with routing_key=retrieval.notify-----')

    remove_reject_data = remove_reject_result['data']

    message = {
        "code": 201,
        "message_type": "retrieval_notification",
        "data": remove_reject_data
    }

    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="retrieval.notify", 
    body=message, properties=pika.BasicProperties(delivery_mode = 2))

    print("\nItem retrieval notification published to RabbitMQ Exchange.\n")


    #---------------------------------------------------------------------------------
    #slack notification for rejected ID

    rejected_slack_item = {"item_id": item["_id"], "item_name": item["itemName"], "buyer_id": rejectedId, "isAccept":False}

    rejected_slack_result = invoke_http(
            f"{slack_url}",
            method="POST",
            json=rejected_slack_item
        )
    
    if rejected_slack_result['code'] not in range(200, 300):
        print('\n\n-----Publishing the (slack error) message with routing_key=slack.error-----')
            
        message = {
            "code": 400,
            "message_type": "business_error",
            "data": "Invalid slack response"
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



