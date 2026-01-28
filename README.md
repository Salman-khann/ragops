# RAG Platform - Local-First AI Knowledge Base

A production-ready RAG (Retrieval-Augmented Generation) platform built with FastAPI, ChromaDB, MinIO, PostgreSQL, and Ollama.

## Features

- 📁 **Document Upload** - Upload text files and PDFs to your knowledge base
- 🤖 **AI-Powered Q&A** - Query documents using local LLMs via Ollama
- 🔍 **Vector Search** - Semantic search using ChromaDB
- 📦 **Object Storage** - MinIO for scalable file storage
- 📊 **Audit Logging** - PostgreSQL for compliance and tracking
- 🎨 **Modern UI** - Clean Flask-based web interface

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Flask + HTML/CSS/JavaScript
- **Vector DB**: ChromaDB
- **Object Storage**: MinIO
- **Database**: PostgreSQL
- **LLM Runtime**: Ollama
- **Containerization**: Docker Compose

## Prerequisites

- Docker and Docker Compose
- Python 3.12+
- 2GB+ RAM (for smaller models like tinyllama)

## Quick Start

### 1. Start Docker Services

```bash
cd ragbackend
docker-compose up -d
```

This will start:
- PostgreSQL (port 5432)
- MinIO (port 9000, console 9001)
- ChromaDB (port 8000)
- Ollama (port 11434)

### 2. Setup Python Environment

```bash
cd ragbackend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Pull a Lightweight LLM Model

```bash
docker exec ragops-ollama ollama pull tinyllama
```

Other options:
- `phi` - Small but capable
- `gemma:2b` - Google's small model

### 4. Start Backend API

```bash
source venv/bin/activate
uvicorn main:app --reload --port 8080
```

Backend will be available at: http://localhost:8080

### 5. Start Frontend

In a new terminal:

```bash
source venv/bin/activate
python frontend.py
```

Frontend will be available at: http://localhost:5000

## Usage

1. **Access the UI**: Open http://localhost:5000 in your browser
2. **Upload Documents**: Use the file uploader to add PDFs or text files
3. **Ask Questions**: Type your query and select a model
4. **Get Answers**: Receive AI-generated responses with source citations

## API Endpoints

### Upload Document
```bash
POST http://localhost:8080/upload
Content-Type: multipart/form-data
```

### Query Knowledge Base
```bash
POST http://localhost:8080/query
Content-Type: application/json
{
  "query": "Your question here",
  "model": "tinyllama"
}
```

## Configuration

Edit the following in `main.py`:

```python
MINIO_ENDPOINT = "localhost:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"
CHROMA_HOST = "localhost"
CHROMA_PORT = 8000
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/ragops"
```

## Troubleshooting

### Memory Issues
If you get "model requires more system memory" errors:
- Use `tinyllama` (smallest, ~637MB)
- Or `phi` (~1.6GB)
- Avoid larger models like `llama3.2` on limited RAM

### Port Already in Use
```bash
# Kill process on port 8080
fuser -k 8080/tcp

# Or use a different port
uvicorn main:app --reload --port 8081
```

### Docker Services Not Starting
```bash
docker-compose down
docker-compose up -d --force-recreate
```

## Project Structure

```
ragops/
├── ragbackend/
│   ├── main.py              # FastAPI backend
│   ├── frontend.py          # Flask frontend server
│   ├── docker-compose.yml   # Docker services
│   ├── requirements.txt     # Python dependencies
│   └── templates/
│       └── index.html       # Web UI
└── README.md
```

## Development

### Adding New Features
1. Update `main.py` for backend logic
2. Modify `templates/index.html` for UI changes
3. Test locally before pushing

### Database Migrations
The app auto-creates tables on startup. For manual control:

```python
await init_db()  # Creates all tables
```

## License

MIT License

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## Author

Built with ❤️ using modern AI/ML technologies
