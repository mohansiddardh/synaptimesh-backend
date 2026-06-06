import time
from dispatcher import dispatch_eeg

demo_values = [

    10,
    20,
    30,
    40,
    50,

    100,
    110,

    120,
    130,

    140,
    150,

    160,
    170,

    180,
    190,
    200,
    210,

    220,
    230,
    240,

    60,
    70,
    80,
    90
]

print("\nEEG Desktop Automation Demo\n")

for value in demo_values:

    print(f"\nEEG Value -> {value}")

    try:

        result = dispatch_eeg(value)

        print(result)

    except Exception as e:

        print(f"ERROR: {e}")

    time.sleep(7)

print("\nDemo Completed")