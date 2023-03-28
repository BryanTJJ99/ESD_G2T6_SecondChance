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
carbon_calculator_url = 'http://localhost:5005/carbon_calc'
create_item_url = 'http://localhost:5006/create'
item_url = 'http://localhost:5007/item'

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

        # ##################### END OF AMQP code
        return old_item_result

    # ##################### AMQP code      

    # handle notification -> item retrieval successful

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

    # ##################### END OF AMQP code

    # CHANGE: replace all the escrows with the right variable plzzz
    if old_item_data["status"] == "pending":
        escrow_result = invoke_http(
            f"{escrow_url}/{old_item_data['item_id']}",
            method="GET"
        )

        if escrow_result["code"] not in range(200,300):
             # ##################### AMQP Code 

             # handle error --> escrow processing fail 

            print('\n\n-----Publishing the escrow error message with routing_key=escrow.error-----') 
        
            message = {
                "code": 400,
                "message_type": "escrow_error",
                "data": escrow_result
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="escrow.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 

            print("\nOrder escrow error published to RabbitMQ Exchange.\n")

            # ##################### END OF AMQP code

            return escrow_result

        escrow_data = escrow_result["data"]

        # ##################### AMQP code 

        # handle notify -> escrow processing notification

        print('\n\n-----Publishing the escrow notification message with routing_key=escrow.notify-----') 


