from kafka import KafkaProducer

TOPIC_NAME = 'leaderboard'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b' hi bryan!!!!')
producer.flush()