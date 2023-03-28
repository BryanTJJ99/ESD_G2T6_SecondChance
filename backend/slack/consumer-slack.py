from kafka import KafkaConsumer
from slack_bolt import App
import json
app = App(token="xoxb-4901815051863-4909773123750-8oLa0zx90HfRPYhSiPzqyOFM")

TOPIC_NAME = 'slack'
KAFKA_SERVER = 'localhost:9092'

def send_message_to_channel(channel_id, message):
    print(message)
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"item ID: {message['id']}"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"item Name: {message['item_name']}"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"creator ID: {message['creatorId']}"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"reciever ID: {message['recievorId']}"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Listed?: {message['isListing']}"
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
    try:
        response = app.client.chat_postMessage(
            channel=channel_id,
            blocks=blocks
        )
        print("Message sent: ", message)
    except Exception as e:
        print("Error sending message: ", e)


# consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda m: json.loads(m.decode('utf-8')))
# for message in consumer:

#     channel_id = "C04SYABL19Q"  # Replace with your channel ID
#     message_text = message.value
    
#     send_message_to_channel(channel_id, message_text)

TOPIC_NAME1 = 'accept'
TOPIC_NAME2 = 'reject'

# Create a Kafka consumer
consumer = KafkaConsumer(
    bootstrap_servers=KAFKA_SERVER,
    group_id='my_group',
    auto_offset_reset='earliest'
)

# Subscribe to the topics
consumer.subscribe(topics=[TOPIC_NAME1, TOPIC_NAME2])

# Read messages from the topics
for message in consumer:

    channel_id = "C04SYABL19Q"  # Replace with your channel ID
    message_text = message.value

    topic = message.topic
    key = message.key
    value = message.value.decode('utf-8')
    if topic == TOPIC_NAME1:
        # Handle messages from topic1 with key1
        if key == 'accepted_key':
            data = json.loads(value)
            print(f"Received message with key={key} from {topic}: {data}")
            send_message_to_channel(channel_id, message_text)
    elif topic == TOPIC_NAME2:
        # Handle messages from topic2 with key2
        if key == 'rejected_key':
            data = json.loads(value)
            print(f"Received message with key={key} from {topic}: {data}")