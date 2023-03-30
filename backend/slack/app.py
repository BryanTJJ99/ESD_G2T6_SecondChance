from kafka import KafkaProducer
import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymongo
from bson import json_util, ObjectId
from dotenv import load_dotenv


load_dotenv()  # load environment variables from .env file

app = Flask(__name__)
CORS(app)

mongodb = os.getenv('MONGODB')
client = pymongo.MongoClient(mongodb)
db = client['ESDProject']
channelCollection = db['channels']


KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME = 'slack'

#get channel ID and send data from producer

@app.route('/slack', methods=['POST'])
def getSlackMsg():
    if request.is_json:
        data = request.get_json()
        #get channelId from MongoDB
        channel = channelCollection.find_one({"departmentID": data["buyerId"]})
        
        if channel is not None:
            channel = json.loads(json_util.dumps(channel))
            
        else:
            print('department do not have a channel ID')

        #decide if message should be accepted or rejected
        accepted_message = {"itemId": data['itemId'], "itemName": data['itemName'], "channelId": channel["channelID"], "token":channel["token"], "message": "accepted"}
        rejected_message = {"itemId": data['itemId'], "itemName": data['itemName'], "channelId": channel["channelID"], "token":channel["token"], "message": "rejected"}

        if data["isAccept"]:
            message = accepted_message
        else:
            message = rejected_message

        #slack configuration
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        print('==================')

        producer.send(TOPIC_NAME, message)
        producer.flush()

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


