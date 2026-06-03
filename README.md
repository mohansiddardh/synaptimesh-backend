# SynaptiMesh Backend

FastAPI backend project.

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload


API Endpoint
eeg Check:
Http
GET /eeg

Response:
JSON
{
  "signal_status": "active",
  "device": "EEG Sensor",
  "message": "EEG monitoring service is running"
}
