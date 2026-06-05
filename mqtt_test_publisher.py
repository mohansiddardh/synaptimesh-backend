import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.publish(
    "eeg/signals",
    '{"eeg_value":0.74}'
)

print("Message Sent")