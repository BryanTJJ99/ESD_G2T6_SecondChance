from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import os, sys

from os import environ

from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

department_url = environ.get('department_URL') or 'http://localhost:8080/department'
carbon_retriever_url = environ.get('carbon_retriever_URL') or 'http://localhost:5002/search'
create_item_url = environ.get('item_URL') or 'http://localhost:5000/create'

@app.route('/place_item', methods=['POST'])
@cross_origin()
def place_item():
    if request.is_json:
        try:
            # item format
            # {
            #   '_id': string,
            #   'itemName': string,
            #   'itemCategory': string,
            #   'isListed': boolean,
            #   'itemPicture': BLOB,
            #   'itemDescription': Null, String,
            #   'carbonEmission': Null, Number,
            #   'receivorId': string (Department),
            #   'companyId': string (Company),
            #   'departmentId': string (Department)
            # }
            item = request.get_json()
            result = process_place_item(item)
            return result
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = f"{str(e)} at {str(exc_type)}: {fname}: line {str(exc_tb.tb_lineno)}"
            print(ex_str)
        
            return jsonify({
                "code": 500,
                "message": f"place_item.py internal error: {ex_str}" 
            })
        
    return jsonify({
        "code": 400,
        "message": f"Invalid JSON input {request.get_data()}"
    })
        
def process_place_item(item):
    amqp_setup.check_setup()
    # get department of item created
    department_result = invoke_http(
        f"{department_url}/{item['departmentId']}",
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
    
    # if department exists
    department_data = department_result['data']

    company_id = department_data['companyId']

    message = {
        "code": 201,
        "message_type": 'department_get_request',
        "data": department_data
    }
    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))

    # department_result return format
    # {
    #   "code": int,
    #   "data": {
    #       "_id": int,
    #       "departmentName": string,
    #       "email": string,
    #       "password": string,
    #       "postalCode": string,
    #       "items": ArrayList<item>,
    #       "totalCarbon": double
    #   }
    # }

    # get carbon emission
    carbon_calculator_result = invoke_http(
        f"{carbon_retriever_url}?name={item['itemCategory']}",
        method='GET'
    )

    carbon_calculator_data = carbon_calculator_result['data']

    if carbon_calculator_result['code'] not in range(200,300):
        code = carbon_calculator_result['code']
        print('\n\n-----Publishing the (carbon calculator error) message with routing_key=carbon_calculator.error-----')
        message = {
            "code": 400,
            "message_type": "carbon_calculator_get_request_error",
            "data": carbon_calculator_data
        }

        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='carbon_calculator.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nCarbon Calculator error - Code {} - published to the RabbitMQ Exchange:".format(code))
        return carbon_calculator_result

    message = {
        "code": 201,
        "message_type": 'carbon_calculator_get_request',
        "data": carbon_calculator_data
    }

    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='carbon_calulator.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))
    
    # add carbon data to item
    item['carbonEmission'] = carbon_calculator_data
    # add companyId to item
    item['companyId'] = company_id
    # post item

    item_result = invoke_http(
        f"{create_item_url}",
        method='POST',
        json=item
    )

    item_result = item_result['data']
    item_data = item_result['data']
    # if post request to create item code fails
    if item_result['code'] not in range(200,300):
        code = item_result['code']
        print('\n\n-----Publishing the (item error) message with routing_key=item.error-----')
        message = {
            "code": 400,
            "message_type": "item_post_error",
            "data": item_data
        }

        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='item.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nItem error - Code {} - published to the RabbitMQ Exchange:".format(code))
        return item_result
    # if post request to create item code works
    message = {
            "code": 201,
            "message_type": 'item_post_request',
            "data": item_data
        }
    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='item.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))

    item_data = item_data['item']

    department_id = item_data['departmentId']
    item_id = item_data['_id']['$oid']
    # add item to department itemIdArrayList
    addItemId_result = invoke_http(
        f'{department_url}/addItemID/{department_id}/{item_id}',
        method='POST'
    )

    # if addItemID does not work
    if addItemId_result['code'] not in range(200,300):
        code = addItemId_result['code']
        print('\n\n-----Publishing the (department error) message with routing_key=department.error-----')
        message = {
            "code": 400,
            "message_type": "department_add_item_id_error",
            "data": addItemId_result
        }

        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nDepartment error - Code {} - published to the RabbitMQ Exchange:".format(code))
        return addItemId_result
    # if addItemID works
    message = {
            "code": 201,
            "message_type": 'department_add_item_id_request',
            "data": addItemId_result
        }
    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))

    return item_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001, debug=True)