from kafka import KafkaProducer
import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)


# Get item added
# @app.route('/slack/<item_id>', methods=['POST'])
# def getSlackMsg(item_id):
#     if request.is_json:
#         item = request.get_json()
#         return jsonify(item)
#     else:
#         data = request.get_data()
#         print(data)
#         return jsonify({"code": 400,
#                         # make the data string as we dunno what could be the actual format
#                         "data": str(data),
#                         "message": "Order should be in JSON."}), 400  # Bad Request input

# if __name__ == '__main__':
#     app.run(debug=True)

#slack configuration
TOPIC_NAME = 'slack'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

# dummy data, data will come from item management
dept_name = 'finance'
img_url = 'https://picsum.photos/id/237/200/300'
data = {'dept_name': dept_name, 'img_url':img_url}


message = json.dumps(data).encode('utf-8')
producer.send(TOPIC_NAME, message)
producer.flush()




