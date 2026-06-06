# mqtt_test.py

from mqtt_client import connect


def run():

    client = connect()

    client.loop_start()

    input("Press Enter to Exit...")

    client.loop_stop()

    client.disconnect()


if __name__ == "__main__":
    run()