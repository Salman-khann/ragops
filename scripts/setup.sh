#!/bin/bash

# Setup script for RAG Knowledge Base

set -e

echo "🚀 Setting up RAG Knowledge Base..."

# Check prerequisites
echo "📋 Checking prerequisites..."
command -v python3 >/dev/null 2>&1 || { echo "❌ Python 3 is required but not installed."; exit 1; }
command -v docker >/dev/null 2>&1 || { echo "❌ Docker is required but not installed."; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo "❌ Docker Compose is required but not installed."; exit 1; }
command -v node >/dev/null 2>&1 || { echo "❌ Node.js is required but not installed."; exit 1; }

echo "✅ All prerequisites met!"

# Setup backend
echo ""
echo "🔧 Setting up backend..."
cd backend

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Backend setup complete!"

# Setup frontend
echo ""
echo "🎨 Setting up frontend..."
cd ../frontend

# Install dependencies
echo "Installing Node dependencies..."
npm install

echo "✅ Frontend setup complete!"

# Start infrastructure
echo ""
echo "🐳 Starting infrastructure services..."
cd ../backend
docker-compose up -d

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Start backend: cd backend && source venv/bin/activate && uvicorn app.main:app --reload --port 8080"
echo "2. Start frontend: cd frontend && npm start"
echo ""
echo "🌐 URLs:"
echo "  - Frontend: http://localhost:3000"
echo "  - Backend API: http://localhost:8080"
echo "  - API Docs: http://localhost:8080/docs"
echo "  - MinIO Console: http://localhost:9001 (minioadmin/minioadmin)"
echo ""
