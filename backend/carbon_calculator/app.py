from flask import Flask, request
import pymongo
import os
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "It works"

# return carbon emission for item
# input is product name and category
@app.route('/search', methods=['POST'])
def insert():
    
    general_emissions = {
        "furniture": 0,
        "office supplies": 0,
        "equipment": 0,
        "electronics": 0,
        "others": 0
    }

    data = request.json
    category = data["category"]
    item_name = data["name"].split(" ")
    found = False
    emissions_data = 0

    # for each in item_name:
        # if collection.find_one({"_id": ObjectId(item_id)}):
            # emissions = collection.find_one({"_id": ObjectId(item_id)})
            # emissions_data = json.loads(json_util.dumps(emissions))
            # found = True

    if not found:
        emissions_data = general_emissions[category]

    return emissions_data
