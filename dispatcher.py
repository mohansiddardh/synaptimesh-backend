import os
import time
import subprocess
import webbrowser
import pyautogui

pyautogui.FAILSAFE = True

THRESHOLD = 0.70

# =====================================================
# APPLICATION FUNCTIONS
# =====================================================

def open_browser():
    webbrowser.open("https://www.google.com")
    return "Browser Opened"


def close_browser():
    os.system("taskkill /F /IM chrome.exe >nul 2>&1")
    os.system("taskkill /F /IM msedge.exe >nul 2>&1")
    os.system("taskkill /F /IM firefox.exe >nul 2>&1")
    return "Browser Closed"


def open_youtube():

    video_url = "https://www.youtube.com/watch?v=jfKfPfyJRdk"

    subprocess.Popen(
        f'start "" "{video_url}"',
        shell=True
    )

    time.sleep(15)

    screen_width, screen_height = pyautogui.size()

    pyautogui.click(
        screen_width // 2,
        screen_height // 2
    )

    time.sleep(2)

    pyautogui.press("k")

    time.sleep(1)

    pyautogui.press("f")

    return "YouTube Video Playing"


def close_youtube():
    os.system("taskkill /F /IM chrome.exe >nul 2>&1")
    os.system("taskkill /F /IM msedge.exe >nul 2>&1")
    os.system("taskkill /F /IM firefox.exe >nul 2>&1")
    return "YouTube Closed"


def open_calculator():
    subprocess.Popen("calc.exe")
    return "Calculator Opened"


def close_calculator():
    os.system("taskkill /F /IM CalculatorApp.exe >nul 2>&1")
    os.system("taskkill /F /IM calc.exe >nul 2>&1")
    return "Calculator Closed"


def open_notepad():
    subprocess.Popen("notepad.exe")
    return "Notepad Opened"


def close_notepad():
    os.system("taskkill /F /IM notepad.exe >nul 2>&1")
    return "Notepad Closed"


# =====================================================
# COMMAND REGISTRY
# =====================================================

COMMAND_REGISTRY = {

    # Browser
    "OPEN_BROWSER": open_browser,
    "CLOSE_BROWSER": close_browser,

    # YouTube
    "OPEN_YOUTUBE": open_youtube,
    "CLOSE_YOUTUBE": close_youtube,

    # Calculator
    "OPEN_CALCULATOR": open_calculator,
    "CLOSE_CALCULATOR": close_calculator,

    # Notepad
    "OPEN_NOTEPAD": open_notepad,
    "CLOSE_NOTEPAD": close_notepad,

    # Media
    "PLAY": lambda: pyautogui.press("playpause"),
    "PAUSE": lambda: pyautogui.press("playpause"),
    "NEXT_TRACK": lambda: pyautogui.press("nexttrack"),
    "PREV_TRACK": lambda: pyautogui.press("prevtrack"),

    # Volume
    "VOLUME_UP": lambda: pyautogui.press("volumeup"),
    "VOLUME_DOWN": lambda: pyautogui.press("volumedown"),
    "MUTE": lambda: pyautogui.press("volumemute"),

    # Scroll
    "SCROLL_UP": lambda: pyautogui.scroll(500),
    "SCROLL_DOWN": lambda: pyautogui.scroll(-500),

    # Mouse Move
    "MOVE_UP": lambda: pyautogui.moveRel(0, -100),
    "MOVE_DOWN": lambda: pyautogui.moveRel(0, 100),
    "MOVE_LEFT": lambda: pyautogui.moveRel(-100, 0),
    "MOVE_RIGHT": lambda: pyautogui.moveRel(100, 0),

    # Mouse Clicks
    "CLICK": lambda: pyautogui.click(),
    "DOUBLE_CLICK": lambda: pyautogui.doubleClick(),
    "RIGHT_CLICK": lambda: pyautogui.rightClick(),

    # Keyboard
    "PRESS_ENTER": lambda: pyautogui.press("enter"),
    "PRESS_ESCAPE": lambda: pyautogui.press("esc"),
}


# =====================================================
# DISPATCH FUNCTION
# =====================================================

def dispatch_command(command_name, confidence):

    cmd = command_name.strip().upper()

    if cmd not in COMMAND_REGISTRY:
        return {
            "status": "error",
            "command": cmd,
            "message": "Command not recognized"
        }

    if confidence < THRESHOLD:
        return {
            "status": "skipped",
            "command": cmd,
            "message": f"Confidence below threshold ({THRESHOLD})"
        }

    try:

        result = COMMAND_REGISTRY[cmd]()

        return {
            "status": "executed",
            "command": cmd,
            "confidence": confidence,
            "message": str(result)
        }

    except Exception as e:

        return {
            "status": "execution_failed",
            "command": cmd,
            "message": str(e)
        }


# =====================================================
# TESTING
# =====================================================

if __name__ == "__main__":

    test_commands = [

        ("OPEN_NOTEPAD", 0.95),
        ("OPEN_CALCULATOR", 0.95),
        ("OPEN_BROWSER", 0.95),
        ("OPEN_YOUTUBE", 0.95),

        ("VOLUME_UP", 0.95),
        ("VOLUME_DOWN", 0.95),

        ("PLAY", 0.95),
        ("PAUSE", 0.95),

        ("SCROLL_DOWN", 0.95),
        ("SCROLL_UP", 0.95),

        ("MOVE_RIGHT", 0.95),
        ("MOVE_LEFT", 0.95),

        ("CLICK", 0.95),

        ("CLOSE_NOTEPAD", 0.95),
        ("CLOSE_CALCULATOR", 0.95),
        ("CLOSE_BROWSER", 0.95)
    ]

    for cmd, conf in test_commands:

        print(f"\nExecuting: {cmd}")

        result = dispatch_command(cmd, conf)

        print(result)

        time.sleep(10)