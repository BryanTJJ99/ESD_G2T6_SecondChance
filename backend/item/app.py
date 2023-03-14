from crypt import methods
from bson import ObjectId
from dotenv import load_dotenv
from flask import Flask, request
import pymongo
import os
from error import *
from bson import json_util, ObjectId
import json

load_dotenv()

app = Flask(__name__)
mongodb = os.getenv('MONGODB')
client = pymongo.MongoClient(mongodb)
db = client['test']
collection = db['items']

@app.route("/")
def home():
    return "It works"

# insert new item
@app.route('/create', methods=['POST'])
def insert():
    data = request.json
    errMsg = handleError(data)
    if errMsg == '':
        collection.insert_one(data)
        return "Created item"
    return errMsg

# read item
@app.route('/<item_id>', methods=['GET'])
def read(item_id):
    item = collection.find_one({"_id": ObjectId(item_id)})
    item = json.loads(json_util.dumps(item))
    return item

# edit item
@app.route('/edit/<item_id>', methods=['PUT'])
def edit(item_id):
    data = request.json
    errMsg = handleError(data)
    if errMsg == '':
        originalQuery = collection.find_one({"_id": ObjectId(item_id)})
        newValues = { "$set": data }
        collection.update_one(originalQuery, newValues)
        return "Item updated"
    return errMsg

# delete item
@app.route('/delete/<item_id>', methods=['DELETE'])
def delete(item_id):
    data = request.json
    errMsg = handleError(data)
    if errMsg == '':
        collection.delete_one({"_id": ObjectId(item_id)})
        return "Item deleted"
    return errMsg

# list item
@app.route('/list/<item_id>', methods=['PUT'])
def addListing(item_id):
    originalQuery = collection.find_one({"_id": ObjectId(item_id)})
    if originalQuery['isListed'] == 0:
        newListing = { "$set": { "isListed": 1 } }
        collection.update_one(originalQuery, newListing)
        return "Item added to listing"
    elif originalQuery['isListed'] == 1:
        newListing = { "$set": { "isListed": 0 } }
        collection.update_one(originalQuery, newListing)
        return "Item removed from listing"

# get all listing in postalCode
@app.route('/postal/<postal_code>', methods=['GET'])
def getPostalCodeItems(postal_code):
    arr = []
    for item in collection.find({'postalCode': int(postal_code)}):
        editedItem = json.loads(json_util.dumps(item))
        arr.append(editedItem)
    return arr

# get all listing in company
@app.route('/company/<company_name>', methods=['GET'])
def getCompanyItems(company_name):
    arr = []
    for item in collection.find({'companyName': company_name}):
        editedItem = json.loads(json_util.dumps(item))
        arr.append(editedItem)
    return arr

if __name__ == '__main__':
    app.run(debug=True)