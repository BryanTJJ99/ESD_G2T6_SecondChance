from kafka import KafkaProducer
import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)


# Get scores
# @app.route('/slack/<dept_id>', methods=['POST'])
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

producer.send(TOPIC_NAME, b' hi this is a test!!!!')
producer.flush()

# producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),bootstrap_servers=KAFKA_SERVER)
# #data will come from item management
# # department_name = getSlackMsg().departmentName
# # image_url = getSlackMsg().isListing.itemPicture
# department_name = 'finance'
# image_URL = 'https://picsum.photos/id/237/200/300'

# message = {
#     "text": f"*{department_name}*",
#     "attachments": [
#         {
#             "fallback": "New items added to the marketplace",
#             "color": "#36a64f",
#             "pretext": "New items added to the marketplace",
#             "image_url": 'image_url'
#         }
#     ]
# }


# producer.send(TOPIC_NAME, message)

# producer.flush()

