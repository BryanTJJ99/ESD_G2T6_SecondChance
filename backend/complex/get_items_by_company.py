from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import os, sys
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

department_url = 'http://localhost:5004/department'
item_url = 'http://localhost:5006/'
company_url = 'http://locahost:5007/'

@app.route('/get_company_items/<department_id>', methods=['GET'])
@cross_origin()
def get_items_by_company(department_id):
    if request.is_json:
        try:
            # department format
            # {
            #   “id”: ObjectId
            #   “departmentName”: String,
            #   “email”: String,
            #   “password”: String
            #   “postalCode”: String,
            #   “Items”: ArrayList<Item>,
            #   “totalCarbon”: double
            # }
            result = process_get_items_by_company(department_id)
            return result
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = f"{str(e)} at {str(exc_type)}: {fname}: line {str(exc_tb.tb_lineno)}"
            print(ex_str)
        
    return jsonify({
        "code": 500,
        "message": f"get_items_by_company.py internal error: {ex_str}" 
    })
        
def process_get_items_by_company(department_id):
    amqp_setup.check_setup()
    # get department data
    department_result = invoke_http(
        f"{department_url}/{department_id}",
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
    #       "companyId": int
    #   }
    # }

    # get company data
    company_result = invoke_http(
        f"{company_url}/{company_id}",
        method="GET"
    )

    company_result = company_result['data']
    company_data = company_result['data']

    if company_result['code'] not in range(200,300):
        code = company_result['code']
        print('\n\n-----Publishing the (company error) message with routing_key=company.error-----')
        message = {
            "code": 400,
            "message_type": "read_company_get_request_error",
            "data": company_data
        }

        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='company.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
        print("\nCompany error - Code {} - published to the RabbitMQ Exchange:".format(code))
        return company_result

    message = {
        "code": 201,
        "message_type": 'read_company_get_request',
        "data": company_data
    }
    message = json.dumps(message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='company.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))

    # get all departments in company
    departments = company_data['departments']

    # get each department in departments to get all items
    itemsList = []
    
    for departmentId in departments:
        department_result = invoke_http(
            f"{department_url}/{departmentId}",
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

        message = {
            "code": 201,
            "message_type": 'department_get_request',
            "data": department_data
        }

        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='department.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))

        # get items in department and concatenate into itemsList
        department_items = department_data['items']
        itemsList += department_items

    # get all items data in itemsList
    result = []
    for itemId in itemsList:
        # read each item
        item_result = invoke_http(
            f"{item_url}/{itemId}",
            method="GET"
        )

        item_result = item_result['data']
        item_data = item_result['data']
        # if get request to read item fails
        if item_result['code'] not in range(200, 300):
            code = item_result['code']
            print('\n\n-----Publishing the (item error) message with routing_key=item.error-----')
            message = {
                "code": 400,
                "message_type": "item_read_error",
                "data": item_data
            }
            message = json.dumps(message)
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='item.error', body=message, properties=pika.BasicProperties(delivery_mode=2))
            print("\nItem error - Code {} - published to the RabbitMQ Exchange:".format(code))
            return item_result
        # if get request works
        result.append(item_data)
        message = {
            "code": 201,
            "message_type": "item_get_request",
            "data": item_data
        }
        message = json.dumps(message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key='item.notify', body=message, properties=pika.BasicProperties(delivery_mode=2))

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)