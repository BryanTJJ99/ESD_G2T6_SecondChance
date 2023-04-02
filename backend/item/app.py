from bson import ObjectId
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pymongo
import os
from error import *
from bson import json_util, ObjectId
import json

load_dotenv()

app = Flask(__name__)
mongodb = os.getenv('MONGODB')
client = pymongo.MongoClient(mongodb)
db = client['ESDProject']
itemCollection = db['items']
userCollection = db['users']
CORS(app)

# get all item
@app.route('/', methods=['GET'])
def getAll():
    items = itemCollection.find()
    items = json.loads(json_util.dumps(items))
    return items

# insert new item
@app.route('/create', methods=['PUT'])
def insert():

    ## format as follows
    # {
    #     "itemName": "Item 1",
    #     "itemCategory": "printer",
    #     "isListed": false,
    #     "itemPicture": "Random Picture",
    #     "itemDescription": "Random Description",
    #     "carbonEmission": { "$numberInt": "880" },
    #     "buyerIds": [],
    #     "companyId": "64227d8d2a884bf918c3d709",
    #     "departmentId": "641d7448835767ff182d7c43"
    # }
    data = request.json
    errMsg = handleError(data)
    if errMsg == '':
        result = itemCollection.insert_one(data)
        item_id = result.inserted_id
        data['_id'] = item_id
        return jsonify({
            "code": 200,
            "data": {
                "item": json.loads(json_util.dumps(data))
            }
        })
    return errMsg

@app.route('/all', methods=['GET'])
def all():
    items = itemCollection.find()
    res = []
    for item in items:
        newItem = json.loads(json_util.dumps(item))
        res.append(newItem)
    return res

# read item
@app.route('/<item_id>', methods=['GET'])
def read(item_id):
    item = itemCollection.find_one({"_id": ObjectId(item_id)})
    item = json.loads(json_util.dumps(item))
    return item

# edit item
@app.route('/edit/<item_id>', methods=['POST'])
def edit(item_id):
    data = request.json
    errMsg = handleError(data)
    if errMsg == '':
        originalQuery = itemCollection.find_one({"_id": ObjectId(item_id)})
        newValues = { "$set": data }
        itemCollection.update_one(originalQuery, newValues)
        data['_id'] = item_id
        return jsonify({
            "code": 200,
            "data": {
                "item": json.loads(json_util.dumps(data))
            }
        })
    return errMsg
    

# delete item
@app.route('/delete/<item_id>', methods=['DELETE'])
def delete(item_id):
    data = request.json
    errMsg = handleError(data)
    if errMsg == '':
        itemCollection.delete_one({"_id": ObjectId(item_id)})
        return "Item deleted"
    return errMsg

# list item
@app.route('/list/<item_id>', methods=['PUT'])
def addListing(item_id):
    originalQuery = itemCollection.find_one({"_id": ObjectId(item_id)})
    if originalQuery['isListed'] == 0:
        newListing = { "$set": { "isListed": 1 } }
        itemCollection.update_one(originalQuery, newListing)
        return "Item added to listing"
    elif originalQuery['isListed'] == 1:
        newListing = { "$set": { "isListed": 0 } }
        itemCollection.update_one(originalQuery, newListing)
        return "Item removed from listing"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)