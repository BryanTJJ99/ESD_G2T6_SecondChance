from kafka import KafkaConsumer
from slack_bolt import App
app = App(token="xoxb-4901815051863-4909773123750-lI9Ug63QZfBfPhJsL2KMArwk")

TOPIC_NAME = 'slack'

def send_message_to_channel(channel_id, message):
    try:
        response = app.client.chat_postMessage(
            channel=channel_id,
            text=message
        )
        print("Message sent: ", message)
    except Exception as e:
        print("Error sending message: ", e)


consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print(message)
    channel_id = "C04SYABL19Q"  # Replace with your channel ID
    message_text = message.value.decode('utf-8')
    send_message_to_channel(channel_id, message_text)