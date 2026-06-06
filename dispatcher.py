import os
import time
import subprocess
import webbrowser
import pyautogui

from logger import logger
from exceptions import InvalidCommandError

pyautogui.FAILSAFE = True

THRESHOLD = 0.70

logger.info("Dispatcher Module Loaded")

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


def open_chatgpt():
    webbrowser.open("https://chatgpt.com")
    return "ChatGPT Opened"


def close_chatgpt():
    os.system("taskkill /F /IM chrome.exe >nul 2>&1")
    os.system("taskkill /F /IM msedge.exe >nul 2>&1")
    os.system("taskkill /F /IM firefox.exe >nul 2>&1")
    return "ChatGPT Closed"


def open_youtube():

    video_url = "https://www.youtube.com"

    subprocess.Popen(
        f'start "" "{video_url}"',
        shell=True
    )

    return "YouTube Opened"


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

    # ChatGPT
    "OPEN_CHATGPT": open_chatgpt,
    "CLOSE_CHATGPT": close_chatgpt,

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

    # Mouse Movement
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
# EEG COMMAND MAPPING
# =====================================================

EEG_COMMANDS = {

    10: "OPEN_NOTEPAD",
    20: "OPEN_CALCULATOR",
    30: "OPEN_BROWSER",
    40: "OPEN_YOUTUBE",
    50: "OPEN_CHATGPT",

    60: "CLOSE_NOTEPAD",
    70: "CLOSE_CALCULATOR",
    80: "CLOSE_BROWSER",
    90: "CLOSE_YOUTUBE",
    100: "CLOSE_CHATGPT",

    110: "VOLUME_UP",
    120: "VOLUME_DOWN",

    130: "PLAY",
    140: "PAUSE",

    150: "NEXT_TRACK",
    160: "PREV_TRACK",

    170: "SCROLL_UP",
    180: "SCROLL_DOWN",

    190: "MOVE_LEFT",
    200: "MOVE_RIGHT",
    210: "MOVE_UP",
    220: "MOVE_DOWN",

    230: "CLICK",
    240: "DOUBLE_CLICK",
    250: "RIGHT_CLICK"
}

# =====================================================
# COMMAND DISPATCHER
# =====================================================

def dispatch_command(command_name, confidence):

    cmd = command_name.strip().upper()

    logger.info(
        f"Command Received: {cmd} | Confidence: {confidence}"
    )

    if cmd not in COMMAND_REGISTRY:

        logger.error(
            f"Invalid Command: {cmd}"
        )

        raise InvalidCommandError(
            f"{cmd} is not a valid command"
        )

    if confidence < THRESHOLD:

        logger.warning(
            f"Low Confidence: {confidence}"
        )

        return {
            "status": "skipped",
            "command": cmd,
            "message": f"Confidence below threshold ({THRESHOLD})"
        }

    try:

        result = COMMAND_REGISTRY[cmd]()

        logger.info(
            f"Executed: {cmd}"
        )

        return {
            "status": "executed",
            "command": cmd,
            "confidence": confidence,
            "message": str(result)
        }

    except Exception as e:

        logger.error(
            f"Execution Failed: {cmd} | {e}"
        )

        raise


# =====================================================
# EEG DISPATCHER
# =====================================================

def dispatch_eeg(eeg_value):

    logger.info(
        f"EEG Value Received: {eeg_value}"
    )

    try:

        eeg_value = int(
            float(eeg_value)
        )

    except Exception:

        logger.error(
            f"Invalid EEG Value: {eeg_value}"
        )

        return {
            "status": "error",
            "message": "Invalid EEG value"
        }

    command = EEG_COMMANDS.get(
        eeg_value
    )

    if command is None:

        logger.warning(
            f"No mapping for EEG value {eeg_value}"
        )

        return {
            "status": "ignored",
            "eeg_value": eeg_value,
            "message": "No command mapped"
        }

    logger.info(
        f"EEG {eeg_value} -> {command}"
    )

    return dispatch_command(
        command,
        0.95
    )


# =====================================================
# LOCAL TESTING
# =====================================================

if __name__ == "__main__":

    test_values = [
        10, 20, 30, 40, 50,
        60, 70, 80, 90, 100,
        110, 120,
        130, 140,
        150, 160,
        170, 180,
        190, 200,
        210, 220,
        230, 240, 250
    ]

    for value in test_values:

        print(f"\nTesting EEG Value: {value}")

        try:

            result = dispatch_eeg(value)

            print(result)

        except Exception as e:

            print(f"ERROR: {e}")

        time.sleep(2)