from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from dispatcher import (
    dispatch_command,
    dispatch_eeg
)

app = FastAPI(
    title="EEG Desktop Automation API",
    version="1.0"
)

# =====================================
# REQUEST MODELS
# =====================================

class CommandPayload(BaseModel):
    command: str
    confidence: float


class EEGPayload(BaseModel):
    eeg_value: float


# =====================================
# HEALTH CHECK
# =====================================

@app.get("/")
def root():
    return {
        "message": "EEG Desktop Automation API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# =====================================
# EEG STATUS
# =====================================

@app.get("/eeg")
def eeg_status():
    return {
        "signal_status": "active",
        "device": "EEG Sensor",
        "message": "EEG monitoring service is running"
    }


# =====================================
# MANUAL COMMAND EXECUTION
# =====================================

@app.post("/dispatch")
def dispatch(payload: CommandPayload):

    result = dispatch_command(
        payload.command,
        payload.confidence
    )

    if result["status"] == "error":
        raise HTTPException(
            status_code=400,
            detail=result["message"]
        )

    return result


# =====================================
# EEG VALUE BASED COMMAND EXECUTION
# =====================================

@app.post("/eeg-command")
def eeg_command(payload: EEGPayload):

    result = dispatch_eeg(
        payload.eeg_value
    )

    return result