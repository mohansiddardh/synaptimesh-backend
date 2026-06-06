import json

from mqtt_client import connect
from dispatcher import dispatch_eeg
from logger import logger

TOPIC = "eeg/signals"

client = connect()


def on_message(client, userdata, msg):

    try:

        payload = json.loads(
            msg.payload.decode()
        )

        eeg_value = payload["eeg_value"]

        result = dispatch_eeg(
            eeg_value
        )

        logger.info(result)

        print(result)

    except Exception as e:

        logger.error(
            f"MQTT Error: {e}"
        )


client.subscribe(TOPIC)

client.on_message = on_message

print("Subscriber Running...")

client.loop_forever()