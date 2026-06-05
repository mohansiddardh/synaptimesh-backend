import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "eeg/commands"

client = mqtt.Client()

def connect():
    client.connect(BROKER, PORT, 60)
    return client