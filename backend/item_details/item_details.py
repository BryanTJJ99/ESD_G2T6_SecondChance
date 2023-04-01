from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import os, sys

import requests
from invokes import invoke_http

from os import environ

import pika
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

department_url = environ.get('department_URL') or 'http://localhost:8080/department'
item_url = environ.get('item_URL') or 'http://localhost:5000/all'
company_url = environ.get('company_URL') or 'http://localhost:5001'

@app.route("/", methods = ['GET'])
@cross_origin()
def getItemDetails():

    main = []

    allItems = invoke_http(
        item_url, method='GET'
        )

    #if allItems does not work
    if allItems['code'] not in range(200,300):
        print("PROBLEMS WITH INVOKING ITEMS MS FROM ITEM_DETAILS")
        code = allItems['code']
        return allItems
    
    #if it works
    allItems_data = allItems['data']

    for ele in allItems_data:
        temp = ele
        department_id = ele['departmentId']
        dept_details = invoke_http(f"{department_url}/{department_id}", method="GET" )

        if dept_details['code'] not in range(200,300):
            print("PROBLEMS WITH INVOKING DEPT FROM ITEMDETAILS")
            return dept_details

        dept_details = dept_details['data']

        temp['department'] = dept_details
        company_ID = dept_details['companyId']
        
        companyDetails =  invoke_http(f"{company_url}/{company_ID}", method="GET")

        if companyDetails['code'] not in range(200,300):
            print("PROBLEMS WITH INVOKING Company FROM ITEMDETAILS")
            return companyDetails
        
        companyDetails = companyDetails['data']

        temp['company'] = companyDetails

        main.append(temp)

    return main
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, debug=True)