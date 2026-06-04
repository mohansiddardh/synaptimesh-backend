from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dispatcher import dispatch_command

app = FastAPI()

class CommandPayload(BaseModel):
    command: str
    confidence: float

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/eeg")
def eeg():
    return {
        "signal_status": "active",
        "device": "EEG Sensor",
        "message": "EEG monitoring service is running"
    }

@app.post("/dispatch")
def dispatch(payload: CommandPayload):
    result = dispatch_command(payload.command, payload.confidence)
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result