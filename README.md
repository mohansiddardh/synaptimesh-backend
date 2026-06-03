# SynaptiMesh Backend

FastAPI backend project.

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload


API Endpoint
Health Check:
Http
GET /health

Response:
JSON
{
  "status": "healthy"
}
