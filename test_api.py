import urllib.request
import urllib.error
import json
import time

def test_endpoint(url, method="GET", data=None, expected_status=200):
    req = urllib.request.Request(url, method=method)
    if data:
        req.data = json.dumps(data).encode('utf-8')
        req.add_header("Content-Type", "application/json")
    
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read().decode('utf-8')
            status = res.status
            print(f"[{method}] {url} -> Status {status} (Expected {expected_status})")
            if status != expected_status:
                print(f"  FAILED: Status code mismatch (Got {status})")
                return False
            print(f"  Response: {body}")
            return json.loads(body)
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8')
        status = e.code
        print(f"[{method}] {url} -> Status {status} (Expected {expected_status})")
        if status != expected_status:
            print(f"  FAILED: Status code mismatch (Got {status})")
            print(f"  Response: {body}")
            return False
        print(f"  Response (Error): {body}")
        try:
            return json.loads(body)
        except Exception:
            return body
    except Exception as e:
        print(f"[{method}] {url} -> Error: {e}")
        return False

def run_tests():
    print("=========================================")
    print("STARTING FASTAPI BACKEND API TESTS")
    print("=========================================")
    
    base_url = "http://127.0.0.1:8000"
    
    # 1. Health Check
    test_endpoint(f"{base_url}/health", expected_status=200)
    
    # 2. EEG Endpoint
    test_endpoint(f"{base_url}/eeg", expected_status=200)
    
    # 3. Dispatch - Valid PLAY
    time.sleep(1)
    test_endpoint(f"{base_url}/dispatch", method="POST", data={"command": "PLAY", "confidence": 0.85}, expected_status=200)
    
    # 4. Dispatch - Low confidence skipped
    time.sleep(1)
    test_endpoint(f"{base_url}/dispatch", method="POST", data={"command": "VOLUME_UP", "confidence": 0.45}, expected_status=200)
    
    # 5. Dispatch - Invalid command error
    time.sleep(1)
    test_endpoint(f"{base_url}/dispatch", method="POST", data={"command": "WAVE_HAND", "confidence": 0.95}, expected_status=400)
    
    print("=========================================")
    print("API TESTS COMPLETED")
    print("=========================================")

if __name__ == "__main__":
    run_tests()
