from kafka import KafkaConsumer
from slack_bolt import App
from json import loads

KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME = 'slack'

def send_message_to_channel(message):

    app = App(token=message["token"])
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Hello your offer for item name: {message['itemName']} (Item ID: {message['itemId']}) is {message['message']}!"
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
            channel=message['channelId'],
            blocks=blocks
        )
        print("Message sent: ", message)
    except Exception as e:
        print("Error sending message: ", e)


consumer = KafkaConsumer(
    TOPIC_NAME,
     bootstrap_servers=['broker:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


for message in consumer:
    # channel_id = "C04SYABL19Q"  # Replace with your channel ID

    message_text = message.value
    send_message_to_channel(message_text)

