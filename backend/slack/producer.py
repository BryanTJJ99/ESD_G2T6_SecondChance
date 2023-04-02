import sys
sys.path.append('/opt/homebrew/lib/python3.9/site-packages')

from time import sleep
from json import dumps
from kafka import KafkaProducer, KafkaConsumer
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from json import loads

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)