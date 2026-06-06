import json
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

# EEG sequence
eeg_values = [
    10,   # Open Notepad
    20,   # Open Calculator
    30,   # Open Browser
    40,   # Open YouTube
    50,   # Open ChatGPT
    100,  # Volume Up
    110,  # Volume Down
    140,  # Next Track
    150,  # Previous Track
    160,  # Scroll Up
    170,  # Scroll Down
    180,  # Mouse Left
    190,  # Mouse Right
    200,  # Mouse Up
    210,  # Mouse Down
    220,  # Click
    230,  # Double Click
    240,  # Right Click
    60,   # Close Notepad
    70,   # Close Calculator
    80,   # Close Browser
    90    # Close YouTube
]

print("EEG Auto Publisher Started")
print("Sending command every 7 seconds...\n")

while True:

    for value in eeg_values:

        payload = {
            "eeg_value": value
        }

        client.publish(
            "eeg/signals",
            json.dumps(payload)
        )

        print(f"Published -> {payload}")

        time.sleep(7)