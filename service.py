# Sample FastAPI Microservice for LLM + RAG (MVP Skeleton)

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

# Mock in-memory store (replace with ChromaDB integration)
vector_stores = {}

# --- Models ---
class AskRequest(BaseModel):
    input: str
    business_id: str

class RegisterBusinessRequest(BaseModel):
    business_id: str

# --- Endpoints ---
@app.post("/register-business")
async def register_business(req: RegisterBusinessRequest):
    if req.business_id in vector_stores:
        return {"status": "Business already registered."}
    vector_stores[req.business_id] = []  # Placeholder for vector DB initialization
    return {"status": "Business registered successfully."}

@app.post("/upload-doc")
async def upload_doc(business_id: str, file: UploadFile = File(...)):
    if business_id not in vector_stores:
        return {"error": "Business not registered."}
    content = await file.read()
    # Here, you would chunk + embed content and store in ChromaDB
    vector_stores[business_id].append(content)
    return {"status": "Document uploaded and processed."}

@app.post("/ask")
async def ask(req: AskRequest):
    if req.business_id not in vector_stores:
        return {"error": "Business not registered."}
    # Here, you would retrieve chunks + query OpenAI (mocked below)
    mock_response = f"[Mocked GPT-3.5 response for input: '{req.input}' for business {req.business_id}]"
    return {"response": mock_response}

@app.get("/status/{business_id}")
async def status(business_id: str):
    if business_id not in vector_stores:
        return {"error": "Business not registered."}
    doc_count = len(vector_stores[business_id])
    return {"business_id": business_id, "documents_uploaded": doc_count}

# --- Run Locally ---
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
