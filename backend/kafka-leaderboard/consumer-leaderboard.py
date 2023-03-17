from kafka import KafkaConsumer

TOPIC_NAME = 'leaderboard'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print(message)






