import time
from dispatcher import dispatch_command

def run_tests():
    print("=========================================")
    print("STARTING COMMAND DISPATCHER INTEGRATION TESTS")
    print("=========================================")
    
    # 11 simulated command payloads covering all requirements
    payloads = [
        # Gating checks (below 0.70 threshold)
        {"command": "PLAY", "confidence": 0.65, "expected_status": "skipped"},
        {"command": "VOLUME_UP", "confidence": 0.45, "expected_status": "skipped"},
        
        # Unrecognized command check
        {"command": "WAVE_HAND", "confidence": 0.95, "expected_status": "error"},
        
        # Valid media commands
        {"command": "PLAY", "confidence": 0.85, "expected_status": "executed"},
        {"command": "PAUSE", "confidence": 0.75, "expected_status": "executed"},
        {"command": "VOLUME_UP", "confidence": 0.90, "expected_status": "executed"},
        {"command": "VOLUME_DOWN", "confidence": 0.80, "expected_status": "executed"},
        
        # Mouse scrolling commands
        {"command": "SCROLL_UP", "confidence": 0.72, "expected_status": "executed"},
        {"command": "SCROLL_DOWN", "confidence": 0.88, "expected_status": "executed"},
        
        # Browser control commands
        {"command": "OPEN_BROWSER", "confidence": 0.95, "expected_status": "executed"},
        {"command": "CLOSE_BROWSER", "confidence": 0.99, "expected_status": "executed"},
    ]
    
    success_count = 0
    
    for idx, payload in enumerate(payloads, start=1):
        cmd = payload["command"]
        conf = payload["confidence"]
        expected = payload["expected_status"]
        
        print(f"\n[Test Case {idx}] Dispatching '{cmd}' with confidence {conf:.2f}")
        
        # Pause slightly between actions to let PyAutoGUI events register and avoid collisions
        time.sleep(1.0)
        
        result = dispatch_command(cmd, conf)
        
        # Print actual results
        print(f"  Result Status: {result.get('status')}")
        print(f"  Result Message: {result.get('message')}")
        
        # Validate status
        if result.get("status") == expected:
            print("  PASSED")
            success_count += 1
        else:
            print(f"  FAILED (Expected: {expected}, Got: {result.get('status')})")
            
    print("\n=========================================")
    print(f"TEST RESULTS: {success_count}/{len(payloads)} CASES PASSED")
    print("=========================================")
    
    if success_count == len(payloads):
        print("ALL TESTS PASSED SUCCESSFULLY!")
    else:
        print("SOME TESTS FAILED.")
        
if __name__ == "__main__":
    run_tests()
