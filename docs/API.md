# API Documentation

## Base URL

```
http://localhost:8080/api/v1
```

## Endpoints

### Health Check

Check if the API is running and services are available.

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy",
  "version": "0.1.0",
  "services": {
    "database": "connected",
    "minio": "connected",
    "chromadb": "connected",
    "ollama": "connected"
  }
}
```

### Upload Document

Upload a document to the knowledge base.

**Endpoint:** `POST /upload/`

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: File upload

**Example (cURL):**
```bash
curl -X POST "http://localhost:8080/api/v1/upload/" \
  -F "file=@document.txt"
```

**Response:**
```json
{
  "status": "success",
  "file": "document.txt",
  "vector_id": "document.txt-uuid"
}
```

### Query Knowledge Base

Query the knowledge base with RAG.

**Endpoint:** `POST /query/`

**Request:**
```json
{
  "query": "What is the main topic?",
  "model": "llama3.2"
}
```

**Example (cURL):**
```bash
curl -X POST "http://localhost:8080/api/v1/query/" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is the main topic?",
    "model": "llama3.2"
  }'
```

**Response:**
```json
{
  "answer": "The main topic is...",
  "context_sources": ["document.txt"],
  "audit_id": 1
}
```

## Models

Available models:
- `llama3.2` (default)
- `llama2`
- `mistral`

## Error Responses

**400 Bad Request:**
```json
{
  "detail": "Validation error message"
}
```

**500 Internal Server Error:**
```json
{
  "detail": "Error message"
}
```

**503 Service Unavailable:**
```json
{
  "detail": "Ollama Error: Connection failed"
}
```
