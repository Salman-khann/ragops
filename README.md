# RAG Knowledge Base Platform

A production-ready RAG (Retrieval-Augmented Generation) application with a FastAPI backend and React frontend.

## 🚀 Features

- **Document Upload**: Upload and process text documents
- **Vector Storage**: ChromaDB for efficient semantic search
- **LLM Integration**: Ollama for local-first AI responses
- **Object Storage**: MinIO for scalable document storage
- **Audit Logging**: PostgreSQL for compliance tracking
- **Modern UI**: React-based interactive interface

## 📁 Project Structure

```
ragops/
├── backend/                    # FastAPI backend application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # Application entry point
│   │   ├── config.py          # Configuration settings
│   │   ├── models.py          # Database models
│   │   ├── schemas.py         # Pydantic schemas
│   │   └── api/               # API endpoints
│   │       ├── __init__.py
│   │       ├── upload.py      # Upload endpoint
│   │       └── query.py       # Query endpoint
│   ├── requirements.txt
│   └── docker-compose.yml     # Infrastructure services
├── frontend/                   # React frontend application
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.js
│   │   │   └── ChatInterface.js
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
├── docs/                       # Documentation
├── tests/                      # Test suite
├── scripts/                    # Utility scripts
├── .env.example               # Environment variables template
├── .gitignore
├── README.md
└── setup.py
```

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: ORM for PostgreSQL
- **ChromaDB**: Vector database
- **MinIO**: S3-compatible object storage
- **Ollama**: Local LLM inference
- **PostgreSQL**: Audit logging database

### Frontend
- **React**: UI library
- **Axios**: HTTP client
- **CSS3**: Styling

### Infrastructure
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker & Docker Compose

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ragops
```

### 2. Setup Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Start Infrastructure Services
```bash
cd backend
docker-compose up -d
```

This starts:
- PostgreSQL (port 5432)
- MinIO (port 9000, console 9001)
- ChromaDB (port 8000)
- Ollama (port 11434)

### 4. Start Backend Server
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --port 8080
```

Backend API: http://localhost:8080
API Docs: http://localhost:8080/docs

### 5. Setup Frontend
```bash
cd frontend
npm install
npm start
```

Frontend UI: http://localhost:3000

## 📝 Configuration

Copy `.env.example` to `.env` and update variables:

```bash
cp .env.example .env
```

Key configurations:
- Database credentials
- MinIO access keys
- Ollama model settings
- ChromaDB connection

## 🐳 Docker Deployment

Build and run the entire stack:

```bash
docker-compose up -d
```

## 📖 API Documentation

### Upload Document
```bash
POST /api/v1/upload
Content-Type: multipart/form-data

{
  "file": <file>
}
```

### Query Knowledge Base
```bash
POST /api/v1/query
Content-Type: application/json

{
  "query": "Your question here",
  "model": "llama3.2"
}
```

## 🧪 Testing

Run tests:
```bash
cd backend
pytest tests/
```

## 📊 Monitoring

- **MinIO Console**: http://localhost:9001
- **API Docs**: http://localhost:8080/docs
- **PostgreSQL**: localhost:5432

## 🔒 Security

- Environment variables for sensitive data
- Input validation with Pydantic
- CORS configuration
- SQL injection protection with ORM

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

MIT License

## 👥 Authors

- Your Name

## 🙏 Acknowledgments

- FastAPI
- React
- Ollama
- ChromaDB
- MinIO
