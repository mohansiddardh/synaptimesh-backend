import time
from mqtt_client import connect, TOPIC
from threshold import EEG_COMMANDS

client = connect()

test_signals = [
    10, 20, 30, 40,
    50, 60,
    90, 100,
    110, 120,
    130, 140,
    150, 160,
    170, 180, 190
]

while True:

    for signal in test_signals:

        command = EEG_COMMANDS.get(signal)

        if command:
            client.publish(TOPIC, command)
            print(f"EEG:{signal} -> {command}")

        time.sleep(10)