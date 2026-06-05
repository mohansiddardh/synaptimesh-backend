# SynaptiMesh Backend

FastAPI backend project.

1. Health Check API

Request

GET /health

URL

http://127.0.0.1:8000/health

Expected Output

{
    "status": "healthy",
    "service": "EEG Control Backend",
    "message": "API is running successfully"
}


---

2. EEG Status API

Request

GET /eeg

URL

http://127.0.0.1:8000/eeg

Expected Output

{
    "signal_status": "active",
    "device": "EEG Sensor",
    "message": "EEG monitoring service is running"
}


---

3. Dispatch Command API

Request

POST /dispatch

URL

http://127.0.0.1:8000/dispatch

Request Body

{
    "command": "PLAY",
    "confidence": 0.85
}

Expected Output

{
    "status": "executed",
    "command": "PLAY",
    "confidence": 0.85,
    "message": "Successfully executed command. Action result: Pressed PLAY/PAUSE media key"
}


---

Supported Commands

Media Controls

PLAY

Request

{
    "command": "PLAY",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "command": "PLAY",
    "confidence": 0.90,
    "message": "Successfully executed command."
}


---

PAUSE

Request

{
    "command": "PAUSE",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "command": "PAUSE",
    "confidence": 0.90
}


---

VOLUME_UP

Request

{
    "command": "VOLUME_UP",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "command": "VOLUME_UP",
    "confidence": 0.90
}


---

VOLUME_DOWN

Request

{
    "command": "VOLUME_DOWN",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "command": "VOLUME_DOWN",
    "confidence": 0.90
}


---

MUTE

Request

{
    "command": "MUTE",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "command": "MUTE",
    "confidence": 0.90
}


---

NEXT_TRACK

Request

{
    "command": "NEXT_TRACK",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "command": "NEXT_TRACK",
    "confidence": 0.90
}


---

PREV_TRACK

Request

{
    "command": "PREV_TRACK",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "command": "PREV_TRACK",
    "confidence": 0.90
}


---

Browser Commands

OPEN_BROWSER

Request

{
    "command": "OPEN_BROWSER",
    "confidence": 0.95
}

Output

{
    "status": "executed",
    "command": "OPEN_BROWSER",
    "confidence": 0.95,
    "message": "Opened Google Chrome"
}

or

{
    "message": "Opened Microsoft Edge"
}


---

CLOSE_BROWSER

Request

{
    "command": "CLOSE_BROWSER",
    "confidence": 0.95
}

Output

{
    "status": "executed",
    "command": "CLOSE_BROWSER",
    "confidence": 0.95,
    "message": "Closed browser processes"
}


---

Mouse Commands

SCROLL_UP

{
    "command": "SCROLL_UP",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "message": "Scrolled up"
}


---

SCROLL_DOWN

{
    "command": "SCROLL_DOWN",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "message": "Scrolled down"
}


---

MOVE_UP

{
    "command": "MOVE_UP",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "message": "Moved mouse up"
}


---

MOVE_DOWN

{
    "status": "executed",
    "message": "Moved mouse down"
}


---

MOVE_LEFT

{
    "status": "executed",
    "message": "Moved mouse left"
}


---

MOVE_RIGHT

{
    "status": "executed",
    "message": "Moved mouse right"
}


---

Click Commands

CLICK

{
    "command": "CLICK",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "message": "Clicked mouse left button"
}


---

DOUBLE_CLICK

{
    "command": "DOUBLE_CLICK",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "message": "Double clicked mouse left button"
}


---

RIGHT_CLICK

{
    "command": "RIGHT_CLICK",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "message": "Clicked mouse right button"
}


---

Keyboard Commands

PRESS_ENTER

{
    "command": "PRESS_ENTER",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "message": "Pressed Enter key"
}


---

PRESS_ESCAPE

{
    "command": "PRESS_ESCAPE",
    "confidence": 0.90
}

Output

{
    "status": "executed",
    "message": "Pressed Escape key"
}


---

Notepad Command (if you added it)

Registry Entry

"OPEN_NOTEPAD": lambda: os.system("start notepad") or "Opened Notepad",

Request

{
    "command": "OPEN_NOTEPAD",
    "confidence": 0.95
}

Output

{
    "status": "executed",
    "command": "OPEN_NOTEPAD",
    "confidence": 0.95,
    "message": "Successfully executed command. Action result: Opened Notepad"
}


---

Low Confidence Output

If confidence is less than 0.70:

Request

{
    "command": "VOLUME_UP",
    "confidence": 0.45
}

Output

{
    "status": "skipped",
    "command": "VOLUME_UP",
    "confidence": 0.45,
    "message": "Command skipped: confidence 0.45 is below threshold 0.70"
}


---

Invalid Command Output

Request

{
    "command": "WAVE_HAND",
    "confidence": 0.95
}

Output

{
    "status": "error",
    "command": "WAVE_HAND",
    "confidence": 0.95,
    "message": "Command 'WAVE_HAND' is not recognized in the registry"
}


