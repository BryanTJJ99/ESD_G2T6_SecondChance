from kafka import KafkaProducer
import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


KAFKA_SERVER = 'localhost:9092'

#Get item added
@app.route('/slack', methods=['POST'])
def getSlackMsg():
    if request.is_json:
        message = request.get_json()
        TOPIC_NAME1 = 'accept'
        TOPIC_NAME2 = 'reject'
        #slack configuration
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

        # Send messages to the topic with the specified key
        accepted_key = b'key1'
        accepted_message = {"item_id": message['item_id'], "item_name": message['item_name'], "message": "Hi, you are accepted!"}
        producer.send(TOPIC_NAME1, key=accepted_key, value=accepted_message)

        rejected_key = b'key2'
        rejected_message = {"item_id": message['item_id'], "item_name": message['item_name'], "message": "Hi, you are rejected!"}
        for i in message["buyer_id"]:
            producer.send(TOPIC_NAME2, key=rejected_key, value=rejected_message)
        print('==================')
        print(message)

        producer.flush()

        return message
    else:
        data = request.get_data()
        print(data)
        return jsonify({"code": 400,
                        # make the data string as we dunno what could be the actual format
                        "data": str(data),
                        "message": "Order should be in JSON."}), 400  # Bad Request input

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage slack ...")
    app.run(host='0.0.0.0', port=5008, debug=True)


