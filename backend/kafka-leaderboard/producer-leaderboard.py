from kafka import KafkaProducer
import json

TOPIC_NAME = 'leaderboard'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'), bootstrap_servers=KAFKA_SERVER)
message = {'department':'finance','score':100}
producer.send(TOPIC_NAME, message)
producer.flush()