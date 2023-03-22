from bson import ObjectId
from dotenv import load_dotenv
from flask import Flask, request
import pymongo
import os
from bson import json_util, ObjectId
import json

load_dotenv()

app = Flask(__name__)
mongodb = os.getenv('MONGODB')
client = pymongo.MongoClient(mongodb)
db = client['ESDProject']
allEmissions = db['emissions']

@app.route("/")
def home():
    return "It works"

# return carbon emission for item
# input is product name and category
@app.route('/search', methods=['GET'])
def search():
    
    generalEmissions = {
        "furniture": 150,
        "office supplies": 50,
        "equipment": 200,
        "electronics": 300,
        "others": 100
    }

    category = request.args.get('category') # use default value repalce 'None'
    name = request.args.get('name')
    itemName = name.split(" ")

    # data = request.json
    # category = data["category"]
    # itemName = data["name"].split(" ")

    found = False
    emissionsData = 0

    for each in itemName:
        each = each.strip().lower()

        if allEmissions.find_one({"itemName": each}):
            emission = allEmissions.find_one({"itemName": each})
            emissionsData = json.loads(json_util.dumps(emission["carbonEmission"]))

            found = True
            break

    if not found:
        emissionsData = generalEmissions[category]

    return str(emissionsData)

if __name__ == '__main__':
    app.run(debug=True)