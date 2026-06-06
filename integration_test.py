import time

from dispatcher import dispatch_command
from exceptions import InvalidCommandError


def run_tests():

    print("=" * 60)
    print("EEG DESKTOP AUTOMATION - INTEGRATION TEST")
    print("=" * 60)

    payloads = [

        # Threshold Tests
        {"command": "PLAY", "confidence": 0.65, "expected": "skipped"},
        {"command": "VOLUME_UP", "confidence": 0.50, "expected": "skipped"},

        # Invalid Command
        {"command": "WAVE_HAND", "confidence": 0.95, "expected": "exception"},

        # Media
        {"command": "PLAY", "confidence": 0.95, "expected": "executed"},
        {"command": "PAUSE", "confidence": 0.95, "expected": "executed"},
        {"command": "VOLUME_UP", "confidence": 0.95, "expected": "executed"},
        {"command": "VOLUME_DOWN", "confidence": 0.95, "expected": "executed"},

        # Browser
        {"command": "OPEN_BROWSER", "confidence": 0.95, "expected": "executed"},
        {"command": "CLOSE_BROWSER", "confidence": 0.95, "expected": "executed"},

        # YouTube
        {"command": "OPEN_YOUTUBE", "confidence": 0.95, "expected": "executed"},
        {"command": "CLOSE_YOUTUBE", "confidence": 0.95, "expected": "executed"},

        # Calculator
        {"command": "OPEN_CALCULATOR", "confidence": 0.95, "expected": "executed"},
        {"command": "CLOSE_CALCULATOR", "confidence": 0.95, "expected": "executed"},

        # Notepad
        {"command": "OPEN_NOTEPAD", "confidence": 0.95, "expected": "executed"},
        {"command": "CLOSE_NOTEPAD", "confidence": 0.95, "expected": "executed"},

        # Scroll
        {"command": "SCROLL_UP", "confidence": 0.95, "expected": "executed"},
        {"command": "SCROLL_DOWN", "confidence": 0.95, "expected": "executed"},

        # Mouse
        {"command": "MOVE_UP", "confidence": 0.95, "expected": "executed"},
        {"command": "MOVE_DOWN", "confidence": 0.95, "expected": "executed"},
        {"command": "MOVE_LEFT", "confidence": 0.95, "expected": "executed"},
        {"command": "MOVE_RIGHT", "confidence": 0.95, "expected": "executed"},

        # Clicks
        {"command": "CLICK", "confidence": 0.95, "expected": "executed"},
        {"command": "DOUBLE_CLICK", "confidence": 0.95, "expected": "executed"},
        {"command": "RIGHT_CLICK", "confidence": 0.95, "expected": "executed"},

        # Keyboard
        {"command": "PRESS_ENTER", "confidence": 0.95, "expected": "executed"},
        {"command": "PRESS_ESCAPE", "confidence": 0.95, "expected": "executed"},
    ]

    passed = 0

    for i, test in enumerate(payloads, start=1):

        print(f"\n[Test Case {i}]")
        print(f"Command    : {test['command']}")
        print(f"Confidence : {test['confidence']}")

        try:

            result = dispatch_command(
                test["command"],
                test["confidence"]
            )

            print("Result:", result)

            if result["status"] == test["expected"]:

                print("PASSED")
                passed += 1

            else:

                print(
                    f"FAILED -> Expected "
                    f"{test['expected']} but got "
                    f"{result['status']}"
                )

        except InvalidCommandError as e:

            if test["expected"] == "exception":

                print("PASSED")
                print(f"Exception Caught: {e}")

                passed += 1

            else:

                print(f"FAILED -> Unexpected Exception: {e}")

        except Exception as e:

            print(f"FAILED -> {e}")

        time.sleep(1)

    print("\n" + "=" * 60)
    print(
        f"FINAL RESULT: {passed}/{len(payloads)} TESTS PASSED"
    )
    print("=" * 60)


if __name__ == "__main__":
    run_tests()