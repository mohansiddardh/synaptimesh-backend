import time
import paho.mqtt.client as mqtt

from logger import logger

BROKER = "localhost"
PORT = 1883


def connect():

    client = mqtt.Client()

    client.reconnect_delay_set(
        min_delay=1,
        max_delay=30
    )

    while True:

        try:

            client.connect(
                BROKER,
                PORT,
                60
            )

            logger.info(
                "MQTT Connected"
            )

            return client

        except Exception as e:

            logger.error(
                f"MQTT Connection Failed: {e}"
            )

            time.sleep(5)