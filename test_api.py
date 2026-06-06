import urllib.request
import urllib.error
import json
import time


BASE_URL = "http://127.0.0.1:8000"


def call_endpoint(
    url,
    method="GET",
    data=None,
    expected_status=200
):

    req = urllib.request.Request(
        url,
        method=method
    )

    if data:

        req.data = json.dumps(
            data
        ).encode("utf-8")

        req.add_header(
            "Content-Type",
            "application/json"
        )

    try:

        with urllib.request.urlopen(req) as response:

            status = response.status

            body = response.read().decode(
                "utf-8"
            )

            print(
                f"[PASS] {method} {url}"
            )

            print(
                f"Status: {status}"
            )

            if status != expected_status:

                print(
                    f"FAILED -> Expected {expected_status}"
                )

                return False

            print(
                f"Response: {body}"
            )

            return True

    except urllib.error.HTTPError as e:

        status = e.code

        body = e.read().decode(
            "utf-8"
        )

        print(
            f"[HTTP ERROR] {method} {url}"
        )

        print(
            f"Status: {status}"
        )

        print(
            f"Response: {body}"
        )

        return status == expected_status

    except Exception as e:

        print(
            f"[ERROR] {method} {url}"
        )

        print(str(e))

        return False


def run_tests():

    print("=" * 60)
    print("FASTAPI BACKEND INTEGRATION TEST")
    print("=" * 60)

    passed = 0
    total = 0

    tests = [

        # Health Check
        {
            "url": f"{BASE_URL}/health",
            "method": "GET",
            "expected": 200
        },

        # Root Endpoint
        {
            "url": f"{BASE_URL}/",
            "method": "GET",
            "expected": 200
        },

        # EEG Endpoint
        {
            "url": f"{BASE_URL}/eeg",
            "method": "GET",
            "expected": 200
        },

        # Valid Command
        {
            "url": f"{BASE_URL}/dispatch",
            "method": "POST",
            "data": {
                "command": "PLAY",
                "confidence": 0.95
            },
            "expected": 200
        },

        # Low Confidence
        {
            "url": f"{BASE_URL}/dispatch",
            "method": "POST",
            "data": {
                "command": "VOLUME_UP",
                "confidence": 0.40
            },
            "expected": 200
        },

        # Invalid Command
        {
            "url": f"{BASE_URL}/dispatch",
            "method": "POST",
            "data": {
                "command": "WAVE_HAND",
                "confidence": 0.95
            },
            "expected": 400
        },

        # EEG Trigger
        {
            "url": f"{BASE_URL}/eeg-command",
            "method": "POST",
            "data": {
                "eeg_value": 0.95
            },
            "expected": 200
        }

    ]

    for test in tests:

        total += 1

        result = call_endpoint(
            url=test["url"],
            method=test["method"],
            data=test.get("data"),
            expected_status=test["expected"]
        )

        if result:
            passed += 1

        time.sleep(1)

    print("\n" + "=" * 60)
    print(
        f"FINAL RESULT: {passed}/{total} TESTS PASSED"
    )
    print("=" * 60)


if __name__ == "__main__":
    run_tests()