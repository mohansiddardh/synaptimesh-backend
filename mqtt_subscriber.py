from mqtt_client import connect, TOPIC
from dispatcher import dispatch_command

client = connect()

def on_message(client, userdata, msg):

    command = msg.payload.decode()

    result = dispatch_command(command, 0.95)

    print(result)

client.subscribe(TOPIC)

client.on_message = on_message

print("Subscriber Running...")

client.loop_forever()