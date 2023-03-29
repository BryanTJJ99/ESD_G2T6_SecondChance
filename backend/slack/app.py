from kafka import KafkaProducer
import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME = 'slack'

#Get item added
@app.route('/slack', methods=['POST'])
def getSlackMsg():
    if request.is_json:
        message = request.get_json()
        accepted_message = {"item_id": message['item_id'], "item_name": message['item_name'], "message": "Hi, you are accepted!"}
        rejected_message = {"item_id": message['item_id'], "item_name": message['item_name'], "message": "Hi, you are rejected!"}
        if message["isAccept"]:
            message = accepted_message
        else:
            message = rejected_message

        #slack configuration
        producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

        print('==================')
        print(message)
        producer.send(TOPIC_NAME, message)
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


