import sys
sys.path.append('/opt/homebrew/lib/python3.9/site-packages')

from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import os
from slack_bolt import App
from flask import Flask, request, jsonify
from flask_cors import CORS

consumer = KafkaConsumer(
    'slack',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))



for message in consumer:
    app = App(token='xoxb-4901815051863-4909773123750-WUDmOhAI0vK0lp5Ov8cNX9sI')
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
    print('Text: ', message['text'])