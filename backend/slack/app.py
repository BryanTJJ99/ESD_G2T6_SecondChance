import sys
sys.path.append('/opt/homebrew/lib/python3.9/site-packages')

from time import sleep
from json import dumps
from kafka import KafkaProducer, KafkaConsumer
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from json import loads
import pymongo
from bson import ObjectId, json_util
import json
from slack_bolt import App

app = Flask(__name__)
CORS(app)

@app.route('/produce', methods=['POST'])
def produce():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda x: 
                            dumps(x).encode('utf-8'))
    data = {'text' : 'accepted'}
    try:
        producer.send('slack', value=data)
        print('Sent message')
    except:
        print('Not working')
    sleep(1)
    return "Message Sent"

@app.route('/consume', methods=['GET'])
def consume():
    mongodb = os.getenv('MONGODB')
    client = pymongo.MongoClient(mongodb)
    db = client['ESDProject']
    tokensCollection = db['tokens']
    token = tokensCollection.find_one({'_id': ObjectId('642a9b6dbb7a5c7eb5a3bb01') })
    token = json.loads(json_util.dumps(token))
    token = token['token']
    consumer = KafkaConsumer(
    'slack',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        app = App(token=token)
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Hello, your offer for the item has been {message.value['text']}!"
                }
            },
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "item image"
                },
                    "block_id": "image4",
                    "image_url": 'https://picsum.photos/id/237/200/300',
                    "alt_text": "item image"
            }
        ]
        app.client.chat_postMessage(
            channel='C04SYABL19Q',
            blocks=blocks
        )
        message = message.value
        return 'Text: ', message['text']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)