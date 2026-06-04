import os
import subprocess
import webbrowser
import time
import pyautogui

# Set safety guard: moving mouse to corners raises pyautogui.FailSafeException
pyautogui.FAILSAFE = True

# Global reference to browser process
browser_process = None

def get_browser_paths():
    paths = []
    # Chrome paths
    for base in [os.environ.get("PROGRAMFILES"), os.environ.get("PROGRAMFILES(X86)"), os.environ.get("LOCALAPPDATA")]:
        if base:
            paths.append((os.path.join(base, "Google", "Chrome", "Application", "chrome.exe"), "Google Chrome"))
    # Edge paths
    for base in [os.environ.get("PROGRAMFILES(X86)"), os.environ.get("PROGRAMFILES")]:
        if base:
            paths.append((os.path.join(base, "Microsoft", "Edge", "Application", "msedge.exe"), "Microsoft Edge"))
    return paths

def open_browser():
    global browser_process
    url = "https://www.google.com"
    
    # Attempt to open Chrome or Edge using their absolute paths
    for path, name in get_browser_paths():
        if os.path.exists(path):
            try:
                browser_process = subprocess.Popen([path, url])
                return f"Opened {name}"
            except Exception:
                pass
                
    # Fallback to standard webbrowser module
    try:
        webbrowser.open(url)
        return "Opened default browser"
    except Exception as e:
        return f"Failed to open browser: {str(e)}"

def close_browser():
    global browser_process
    # Attempt to terminate subprocess if tracked
    if browser_process:
        try:
            browser_process.terminate()
            browser_process = None
        except Exception:
            pass
            
    # Send Alt+F4 hotkey to close the active browser window
    try:
        pyautogui.hotkey('alt', 'f4')
    except Exception:
        pass
        
    # Also run taskkill on standard browsers on Windows to ensure they close in automated runs
    os.system("taskkill /f /im chrome.exe >nul 2>&1")
    os.system("taskkill /f /im msedge.exe >nul 2>&1")
    return "Closed browser processes"

# Helper for scroll left
def scroll_left():
    try:
        pyautogui.hscroll(-150)
    except AttributeError:
        pyautogui.keyDown('shift')
        pyautogui.scroll(-150)
        pyautogui.keyUp('shift')
    return "Scrolled left"

# Helper for scroll right
def scroll_right():
    try:
        pyautogui.hscroll(150)
    except AttributeError:
        pyautogui.keyDown('shift')
        pyautogui.scroll(150)
        pyautogui.keyUp('shift')
    return "Scrolled right"

# Command Registry mapping command string names to executing lambdas/functions
COMMAND_REGISTRY = {
    # Media Controls
    "PLAY": lambda: pyautogui.press('playpause') or "Pressed PLAY/PAUSE media key",
    "PAUSE": lambda: pyautogui.press('playpause') or "Pressed PLAY/PAUSE media key",
    "VOLUME_UP": lambda: pyautogui.press('volumeup') or "Pressed VOLUME_UP key",
    "VOLUME_DOWN": lambda: pyautogui.press('volumedown') or "Pressed VOLUME_DOWN key",
    "MUTE": lambda: pyautogui.press('volumemute') or "Pressed MUTE key",
    "NEXT_TRACK": lambda: pyautogui.press('nexttrack') or "Pressed NEXT_TRACK key",
    "PREV_TRACK": lambda: pyautogui.press('prevtrack') or "Pressed PREV_TRACK key",
  
    # Browser Controls
    "OPEN_BROWSER": open_browser,
    "CLOSE_BROWSER": close_browser,
  
    # Mouse Scroll & Move
    "SCROLL_UP": lambda: pyautogui.scroll(250) or "Scrolled up",
    "SCROLL_DOWN": lambda: pyautogui.scroll(-250) or "Scrolled down",
    "SCROLL_LEFT": scroll_left,
    "SCROLL_RIGHT": scroll_right,
    "MOVE_UP": lambda: pyautogui.moveRel(0, -100) or "Moved mouse up",
    "MOVE_DOWN": lambda: pyautogui.moveRel(0, 100) or "Moved mouse down",
    "MOVE_LEFT": lambda: pyautogui.moveRel(-100, 0) or "Moved mouse left",
    "MOVE_RIGHT": lambda: pyautogui.moveRel(100, 0) or "Moved mouse right",
    
    # Click Controls
    "CLICK": lambda: pyautogui.click() or "Clicked mouse left button",
    "DOUBLE_CLICK": lambda: pyautogui.doubleClick() or "Double clicked mouse left button",
    "RIGHT_CLICK": lambda: pyautogui.rightClick() or "Clicked mouse right button",
    
    # Keyboard Controls
    "PRESS_ENTER": lambda: pyautogui.press('enter') or "Pressed Enter key",
    "PRESS_ESCAPE": lambda: pyautogui.press('escape') or "Pressed Escape key",
}

def dispatch_command(command_name: str, confidence: float):
    """
    Validates the command against the registry and confidence threshold.
    Gating: confidence < 0.70 will skip execution.
    """
    # Normalize command name
    cmd_upper = command_name.strip().upper()
    
    if cmd_upper not in COMMAND_REGISTRY:
        return {
            "status": "error",
            "command": command_name,
            "confidence": confidence,
            "message": f"Command '{command_name}' is not recognized in the registry"
        }
        
    if confidence < 0.70:
        return {
            "status": "skipped",
            "command": cmd_upper,
            "confidence": confidence,
            "message": f"Command skipped: confidence {confidence:.2f} is below threshold 0.70"
        }
        
    # Execute command action
    try:
        action = COMMAND_REGISTRY[cmd_upper]
        result = action()
        return {
            "status": "executed",
            "command": cmd_upper,
            "confidence": confidence,
            "message": f"Successfully executed command. Action result: {result}"
        }
    except Exception as e:
        return {
            "status": "execution_failed",
            "command": cmd_upper,
            "confidence": confidence,
            "message": f"Failed to execute command: {str(e)}"
        }
