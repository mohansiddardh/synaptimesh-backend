import time
from dispatcher import dispatch_command

def run_tests():

    print("=" * 50)
    print("STARTING COMMAND DISPATCHER INTEGRATION TESTS")
    print("=" * 50)

    payloads = [

        # Confidence threshold tests
        {"command": "PLAY", "confidence": 0.65, "expected": "skipped"},
        {"command": "VOLUME_UP", "confidence": 0.50, "expected": "skipped"},

        # Invalid command
        {"command": "WAVE_HAND", "confidence": 0.95, "expected": "error"},

        # Media commands
        {"command": "PLAY", "confidence": 0.95, "expected": "executed"},
        {"command": "PAUSE", "confidence": 0.95, "expected": "executed"},
        {"command": "VOLUME_UP", "confidence": 0.95, "expected": "executed"},
        {"command": "VOLUME_DOWN", "confidence": 0.95, "expected": "executed"},

        # Browser commands
        {"command": "OPEN_BROWSER", "confidence": 0.95, "expected": "executed"},
        {"command": "CLOSE_BROWSER", "confidence": 0.95, "expected": "executed"},

        # YouTube commands
        {"command": "OPEN_YOUTUBE", "confidence": 0.95, "expected": "executed"},
        {"command": "CLOSE_YOUTUBE", "confidence": 0.95, "expected": "executed"},

        # Calculator commands
        {"command": "OPEN_CALCULATOR", "confidence": 0.95, "expected": "executed"},
        {"command": "CLOSE_CALCULATOR", "confidence": 0.95, "expected": "executed"},

        # Notepad commands
        {"command": "OPEN_NOTEPAD", "confidence": 0.95, "expected": "executed"},
        {"command": "CLOSE_NOTEPAD", "confidence": 0.95, "expected": "executed"},

        # Mouse commands
        {"command": "SCROLL_UP", "confidence": 0.95, "expected": "executed"},
        {"command": "SCROLL_DOWN", "confidence": 0.95, "expected": "executed"},

        {"command": "MOVE_UP", "confidence": 0.95, "expected": "executed"},
        {"command": "MOVE_DOWN", "confidence": 0.95, "expected": "executed"},
        {"command": "MOVE_LEFT", "confidence": 0.95, "expected": "executed"},
        {"command": "MOVE_RIGHT", "confidence": 0.95, "expected": "executed"},

        # Mouse clicks
        {"command": "CLICK", "confidence": 0.95, "expected": "executed"},
        {"command": "DOUBLE_CLICK", "confidence": 0.95, "expected": "executed"},
        {"command": "RIGHT_CLICK", "confidence": 0.95, "expected": "executed"},

        # Keyboard commands
        {"command": "PRESS_ENTER", "confidence": 0.95, "expected": "executed"},
        {"command": "PRESS_ESCAPE", "confidence": 0.95, "expected": "executed"},
    ]

    passed = 0

    for i, test in enumerate(payloads, start=1):

        print(f"\n[Test Case {i}]")
        print(f"Command: {test['command']}")
        print(f"Confidence: {test['confidence']}")

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
                f"FAILED (Expected {test['expected']} "
                f"but got {result['status']})"
            )

        time.sleep(2)

    print("\n" + "=" * 50)
    print(f"TEST RESULTS: {passed}/{len(payloads)} PASSED")
    print("=" * 50)

if __name__ == "__main__":
    run_tests()