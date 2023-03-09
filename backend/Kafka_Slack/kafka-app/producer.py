from kafka import KafkaProducer

TOPIC_NAME = 'slack'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'hi vicky!!!!')
producer.flush()