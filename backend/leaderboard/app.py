from kafka import KafkaProducer
import json
from error import *
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from bson import ObjectId
from dotenv import load_dotenv
import pymongo
from bson import json_util, ObjectId


app = Flask(__name__)
CORS(app)
mongodb = os.getenv('MONGODB')
client = pymongo.MongoClient(mongodb)
db = client['test']
deptCollection = db['department']

@app.route('/leaderboard', methods=['GET'])
def getDeptID():
    score = deptCollection.find()
    score = json.loads(json_util.dumps(score))
    if request.is_json:
        score = request.get_json()
        result = processScore(score)
        return jsonify(result)
    else:
        data = request.get_data()
        print(data)
        return jsonify({"code": 400,
                        # make the data string as we dunno what could be the actual format
                        "data": str(data),
                        "message": "Order should be in JSON."}), 400  # Bad Request input

# Get scores
   

def processScore(score):
    print("Processing score:")
    # print(score)
    # get the first 5 score and sort it descending order
    score_sorted = sorted(score, key=lambda x: x['age'], reverse=True)
    first_5_score = score_sorted[0:4]
    # If contains "ERROR", simulate failure
    if "ERROR" in score['customer_id']:
        code = 400
        message = 'Simulated failure in leaderboard generation.'
    else:  # simulate success
        code = 201
        message = 'Simulated success in leaderboard generation.'

    print(message)
    print()  # print a new line feed as a separator

    return {
        'code': code,
        'data': {
            'score': first_5_score
        },
        'message': message
    }


if __name__ == '__main__':
    app.run(debug=True)

TOPIC_NAME = 'leaderboard'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'), bootstrap_servers=KAFKA_SERVER)
message = getDeptID
producer.send(TOPIC_NAME, message)
producer.flush()

