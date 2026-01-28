# Project Structure - Cookiecutter Pattern Applied

Your RAG Knowledge Base project has been successfully reorganized following the cookiecutter pattern and best practices.

## 📁 Directory Structure

```
ragops/
├── README.md                    # Main project documentation
├── .gitignore                   # Git ignore rules
├── .env.example                # Environment variables template
├── setup.py                     # Python package setup
├── CONTRIBUTING.md              # Contributing guidelines
│
├── backend/                     # Backend Application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py             # FastAPI application entry
│   │   ├── models.py           # Database models
│   │   ├── schemas.py          # Pydantic schemas
│   │   ├── core/               # Core functionality
│   │   │   ├── config.py       # Configuration settings
│   │   │   ├── database.py     # Database connection
│   │   │   ├── storage.py      # MinIO client
│   │   │   └── vector_db.py    # ChromaDB client
│   │   └── api/                # API endpoints
│   │       ├── health.py       # Health check
│   │       ├── upload.py       # File upload
│   │       └── query.py        # RAG query
│   ├── tests/                  # Test suite
│   │   ├── conftest.py
│   │   └── test_health.py
│   ├── requirements.txt        # Python dependencies
│   ├── docker-compose.yml      # Infrastructure services
│   ├── pytest.ini              # Test configuration
│   └── .env                    # Environment variables
│
├── frontend/                    # React Frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.js   # File upload component
│   │   │   ├── FileUpload.css
│   │   │   ├── ChatInterface.js # Chat component
│   │   │   └── ChatInterface.css
│   │   ├── App.js              # Main app component
│   │   ├── App.css
│   │   ├── index.js            # Entry point
│   │   └── index.css
│   └── package.json            # Node dependencies
│
├── docs/                        # Documentation
│   ├── API.md                  # API documentation
│   └── DEPLOYMENT.md           # Deployment guide
│
└── scripts/                     # Utility scripts
    ├── setup.sh                # Project setup
    ├── start.sh                # Start all services
    ├── stop.sh                 # Stop all services
    └── test.sh                 # Run tests
```

## 🎯 Key Improvements

### Backend Structure
- **Modular Organization**: Separated concerns into `api/`, `core/`, and root modules
- **Configuration Management**: Centralized settings in `core/config.py` with pydantic-settings
- **Clean API Structure**: Separate routers for each endpoint
- **Proper Service Layer**: Storage, database, and vector DB clients in `core/`
- **Testing Suite**: pytest configuration with async support

### Frontend Structure
- **Updated API URLs**: Now pointing to `/api/v1` prefix
- **Component Organization**: Clear separation of concerns
- **Proper Structure**: Standard React project layout

### Documentation
- **Comprehensive README**: Setup instructions, tech stack, API overview
- **API Documentation**: Detailed endpoint documentation
- **Deployment Guide**: Production deployment strategies
- **Contributing Guidelines**: Development workflow

### DevOps
- **Executable Scripts**: Quick setup, start, stop, and test commands
- **Environment Management**: `.env.example` template
- **Git Ignore**: Comprehensive ignore rules
- **Docker Setup**: Isolated infrastructure services

## 🚀 Quick Start Commands

```bash
# Complete setup
./scripts/setup.sh

# Start all services
./scripts/start.sh

# Stop all services
./scripts/stop.sh

# Run tests
./scripts/test.sh
```

## 🌐 Service URLs

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8080
- **API Documentation**: http://localhost:8080/docs
- **Alternative API Docs**: http://localhost:8080/redoc
- **Health Check**: http://localhost:8080/api/v1/health
- **MinIO Console**: http://localhost:9001 (minioadmin/minioadmin)

## 📝 API Endpoints

- `GET /` - Root endpoint
- `GET /api/v1/health` - Health check
- `POST /api/v1/upload/` - Upload document
- `POST /api/v1/query/` - Query knowledge base

## 🧪 Testing

The backend includes a testing suite with:
- **pytest** configuration
- **Async test support**
- **Coverage reporting**
- **Test fixtures**

Run tests with:
```bash
cd backend
pytest tests/ -v --cov=app
```

## 🔒 Security Features

- Environment-based configuration
- Pydantic validation
- CORS configuration
- SQLAlchemy ORM (SQL injection protection)
- Async database operations

## 📦 Dependencies Management

### Backend
- Managed via `requirements.txt`
- Virtual environment isolated
- Development dependencies available

### Frontend  
- Managed via `package.json`
- Modern React ecosystem
- Axios for HTTP requests

## 🔄 Next Steps

1. Copy `.env.example` to `.env` and customize
2. Run `./scripts/setup.sh`
3. Start services with `./scripts/start.sh`
4. Access frontend at http://localhost:3000
5. Upload documents and start querying!

## 📚 Additional Resources

- See `/docs/API.md` for detailed API documentation
- See `/docs/DEPLOYMENT.md` for production deployment
- See `CONTRIBUTING.md` for development guidelines
