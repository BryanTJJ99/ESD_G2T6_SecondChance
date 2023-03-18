from kafka import KafkaConsumer
import json

TOPIC_NAME = 'leaderboard'

consumer = KafkaConsumer(TOPIC_NAME)
consumer = KafkaConsumer(TOPIC_NAME, value_deserializer=lambda v: json.loads(v.decode('utf-8')))

for message in consumer:
    print(message)






