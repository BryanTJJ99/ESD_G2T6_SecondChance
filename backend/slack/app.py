from kafka import KafkaProducer
import json
from json import dumps
from os import environ
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymongo
from bson import json_util, ObjectId
from dotenv import load_dotenv
from error import *

load_dotenv()  # load environment variables from .env file

app = Flask(__name__)
CORS(app)

mongodb = os.getenv('MONGODB')
client = pymongo.MongoClient(mongodb)
db = client['ESDProject']
channelCollection = db['channels']

TOPIC_NAME = 'slack'

#post slack channel to channel collection
@app.route('/slack/add/<department_id>', methods=['POST'])
def addSlackChannel(department_id):
    data = request.json
    errMsg = handleError(data)
    if errMsg == '':
        originalQuery = channelCollection.find_one({"departmentID": ObjectId(department_id)})
        newValues = { "$set": data }
        channelCollection.update_one(originalQuery, newValues)

        return jsonify({
            "code": 200,
            "data": {
                "item": json.loads(json_util.dumps(data))
            }
        })
    return errMsg
    

#get channel ID and send data from producer
@app.route('/slack', methods=['POST'])
def getSlackMsg():
    if request.is_json:
        data = request.get_json()

        #get channelId from MongoDB
        channel = channelCollection.find_one({"departmentID": '641d7448835767ff182d7c43'})
        
        if channel is not None:
            channel = json.loads(json_util.dumps(channel))
            
        else:
            err_msg = 'department do not have a channel ID'
            print(err_msg)
            return err_msg

        #decide if message should be accepted or rejected
        accepted_message = {"itemId": data['itemId'], "itemName": data['itemName'], "channelId": channel["channelID"], "token":channel["token"], "message": "accepted"}
        rejected_message = {"itemId": data['itemId'], "itemName": data['itemName'], "channelId": channel["channelID"], "token":channel["token"], "message": "rejected"}

        if data["isAccept"]:
            message = accepted_message
        else:
            message = rejected_message

        print(f'Message: ', message)

        #slack configuration
        producer = KafkaProducer(bootstrap_servers=['broker:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
        
        message = json.dumps(message)
        producer.send(TOPIC_NAME, message)
        print('==================')

        return message
    else:
        data = request.get_data()
        return jsonify({"code": 400,
                        # make the data string as we dunno what could be the actual format
                        "data": str(data),
                        "message": "Order should be in JSON."}), 400  # Bad Request input

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage slack ...")
    app.run(host='0.0.0.0', port=5008, debug=True)


