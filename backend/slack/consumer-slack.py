from kafka import KafkaConsumer
from slack_bolt import App
import json
app = App(token="xoxb-4901815051863-4909773123750-yoz2pFRyJk4BuVkUULJuBnqH")

TOPIC_NAME = 'slack'
KAFKA_SERVER = 'localhost:9092'

def send_message_to_channel(channel_id, message):
    print(message)
    blocks = [
    {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Department Name: {message['dept_name']}!"
            }
        },
        {
			"type": "image",
			"title": {
				"type": "plain_text",
				"text": "item image"
			},
                "block_id": "image4",
                "image_url": message['img_url'],
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


consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER, value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer:

    channel_id = "C04SYABL19Q"  # Replace with your channel ID
    message_text = message.value
    send_message_to_channel(channel_id, message_text)
