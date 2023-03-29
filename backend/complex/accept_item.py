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
# carbon_calculator_url = 'http://localhost:5005/carbon_calc'
# create_item_url = 'http://localhost:5006/create'
item_url = 'http://localhost:5000/item'
slack_url = 'http://localhost:5008/slack'


@app.route("/accept_item", methods=['POST'])
@cross_origin()
def accept_item():
    if request.is_json:
        try:
            result = process_accept_item(request.json)
            
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


def process_accept_item(request):
    item = request["item"]
    buyerId = request["buyerId"]

    if item["isListed"] == True:
  #---------------------------------------------------------------------------------
    #invoke department url to update changes to seller's database
        seller_department_result = invoke_http(
            f"{department_url}/deleteItemID/{item['departmentId']}/{item['_id']}",
            method='DELETE'
        )
        print(item['departmentId'],item['_id'])
        if seller_department_result['code'] not in range(200,300):
            print('\n\n-----Publishing the (seller department error) message with routing_key=department.error-----')
            print(seller_department_result)
            message = {
                "code": 400,
                "message_type": "department_error",
                "data": seller_department_result['data']
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(seller_department_result['code']))
            return seller_department_result
        else:
            message = {
                "code": 201,
                "message_type": 'department_put_request',
                "data": seller_department_result['data']
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("------------ DEPARTMENT EDITED SUCCESSFULLY - {} ------------".format(seller_department_result))

#---------------------------------------------------------------------------------
    #invoke department url to update changes to buyer's database
        buyer_department_result = invoke_http(
            f"{department_url}/addItemID/{item['departmentId']}/{item['_id']}",
            method='POST'
        )
        if buyer_department_result['code'] not in range(200,300):
            print('\n\n-----Publishing the (buyer department error) message with routing_key=department.error-----')

            message = {
                "code": 400,
                "message_type": "department_error",
                "data": buyer_department_result['data']
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(buyer_department_result['code']))
            return buyer_department_result
        else:
            message = {
                "code": 201,
                "message_type": 'department_put_request',
                "data": buyer_department_result
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("------------ DEPARTMENT EDITED SUCCESSFULLY - {} ------------".format(buyer_department_result))


    #--------------------------------------------------------------------------------
    #getting the rejected list and accepted buyer id
        buyer_list = item['buyerId']
        for id in buyer_list:
            if buyerId == id:
                buyer_list.pop(id)
        rejected_list = buyer_list

    #---------------------------------------------------------------------------------
    #slack notification for accepted buyer
        buyer_slack_item = {"item_id": item["_id"], "item_name": item["itemName"], "buyer_id": buyerId, "isAccept":True}
    
        buyer_slack_result = invoke_http(
                f"{slack_url}",
                method="POST",
                json=buyer_slack_item
            )
        
        
        if buyer_slack_result['code'] not in range(200, 300):
            print('\n\n-----Publishing the (slack error) message with routing_key=slack.error-----')
                
            message = {
                "code": 400,
                "message_type": "business_error",
                "data": "Invalid slack response"
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='slack.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("\nSlack error - Code {} - published to the RabbitMQ Exchange:".format(buyer_slack_result['code']))
            return buyer_slack_result
        
        else:
            message = {
                "code": 201,
                    "message_type": 'slack_notification',
                    "data": buyer_slack_result['data']
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='slack.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("------------ SLACK NOTIFICATION SENT SUCCESSFULLY - {} ------------".format(buyer_slack_result['data']))

    #---------------------------------------------------------------------------------
    #slack notification for rejected list
        for rejectedId in rejected_list:
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


    #---------------------------------------------------------------------------------
    #change status of isListing from true to false, change ownership of item, clear buyer list
            updated_item = {
                "_id": item['_id'],
                "itemName": item['itemName'],
                "itemCategory": item["itemCategory"],
                "isListed": False,
                "itemPicture": item["itemPicture"],
                "itemDescription": item["itemDescription"],
                "carbonEmission": item["carbonEmission"],
                "buyerId": [],
                "companyId": item["companyId"],
                "departmentId": buyerId
            }

            updated_item_result = invoke_http(
                f"{item_url}/edit/{item['_id']}",
                method="PUT",
                json=updated_item,
            )  
                 
            if updated_item_result['code'] not in range(200,300):
                print('\n\n-----Publishing the (updating ownership error) message with routing_key=ownership.error-----')
                message = {
                    "code": 400,
                    "message_type": "ownership_error",
                    "data": updated_item_result
                }

                message = json.dumps(message)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='ownership.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(updated_item_result['code']))
                return updated_item_result
            
            else:
                message = {
                    "code": 201,
                    "message_type": 'department_ownership_put_request',
                    "data": updated_item_result
                }
                message = json.dumps(message)
                amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='ownership.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
                print("------------ OWNERSHIP EDITED SUCCESSFULLY - {} ------------".format(updated_item_result))
            
                print("\nItem accept notification published to RabbitMQ Exchange.\n")

    #---------------------------------------------------------------------------------


        amqp_setup.check_setup()
     

    #---------------------------------------------------------------------------------
    #handle error for 'change status of isListing from true to false
    else:
        return jsonify({
            "code": 403,
            "message": f"Unable to accept item."
        })

    # ##################### END OF AMQP code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5101, debug=True)

