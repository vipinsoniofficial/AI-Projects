# --- README.md ---
# FastAPI RAG Microservice

## Description
Simple FastAPI service to demonstrate multi-tenant LLM+RAG (Retrieval Augmented Generation) engine for AI Voice Assistants.

## Features
- Register new businesses
- Upload business-specific documents
- Ask questions to business-specific knowledgebase
- Mocked vector storage (can be replaced with ChromaDB)

## Setup Instructions
```bash
# Clone the repo
$ git clone <repo-url>

# Navigate to project directory
$ cd project-directory

# Install dependencies
$ pip install fastapi uvicorn pydantic

# Run the app
$ uvicorn app:app --reload
```

## API Endpoints
| Endpoint | Method | Description |
|:---|:---|:---|
| `/register-business` | POST | Register a new business |
| `/upload-doc` | POST | Upload document for business |
| `/ask` | POST | Ask a question |
| `/status/{business_id}` | GET | Check status |

## Docker Instructions
```bash
# Build the Docker image
$ docker build -t fastapi-rag-service .

# Run the container
$ docker run -p 8000:8000 fastapi-rag-service
```
