from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from logger import logger
from dispatcher import (
    dispatch_command,
    dispatch_eeg
)

from exceptions import InvalidCommandError

logger.info("Server Starting")

app = FastAPI(
    title="EEG Desktop Automation API",
    version="1.0"
)

# =====================================
# GLOBAL EXCEPTION HANDLER
# =====================================

@app.exception_handler(
    InvalidCommandError
)
async def invalid_command_handler(
    request,
    exc
):

    logger.error(
        f"Invalid Command Error: {str(exc)}"
    )

    return JSONResponse(
        status_code=400,
        content={
            "status": "error",
            "message": str(exc)
        }
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

    logger.info("Root endpoint accessed")

    return {
        "message": "EEG Desktop Automation API Running"
    }


@app.get("/health")
def health():

    logger.info("Health endpoint accessed")

    return {
        "status": "healthy"
    }


# =====================================
# EEG STATUS
# =====================================

@app.get("/eeg")
def eeg_status():

    logger.info("EEG status checked")

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

    logger.info(
        f"Command Received: {payload.command}, Confidence: {payload.confidence}"
    )

    try:

        result = dispatch_command(
            payload.command,
            payload.confidence
        )

        logger.info(
            f"Command Executed Successfully: {payload.command}"
        )

        return result

    except InvalidCommandError:

        raise

    except Exception as e:

        logger.error(
            f"Dispatch Error: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =====================================
# EEG VALUE BASED COMMAND EXECUTION
# =====================================

@app.post("/eeg-command")
def eeg_command(payload: EEGPayload):

    logger.info(
        f"EEG Value Received: {payload.eeg_value}"
    )

    try:

        result = dispatch_eeg(
            payload.eeg_value
        )

        logger.info(
            f"EEG Processing Result: {result}"
        )

        return result

    except Exception as e:

        logger.error(
            f"EEG Processing Error: {str(e)}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )