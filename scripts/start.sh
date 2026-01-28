#!/bin/bash

# Start all services

set -e

echo "🚀 Starting RAG Knowledge Base..."

# Start infrastructure
echo "🐳 Starting infrastructure services..."
cd backend
docker-compose up -d

# Wait for services
echo "⏳ Waiting for services..."
sleep 5

# Start backend
echo "🔧 Starting backend..."
source venv/bin/activate
uvicorn app.main:app --reload --port 8080 &
BACKEND_PID=$!

# Start frontend
echo "🎨 Starting frontend..."
cd ../frontend
npm start &
FRONTEND_PID=$!

echo ""
echo "✅ All services started!"
echo ""
echo "🌐 URLs:"
echo "  - Frontend: http://localhost:3000"
echo "  - Backend API: http://localhost:8080"
echo "  - API Docs: http://localhost:8080/docs"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for user interrupt
trap "kill $BACKEND_PID $FRONTEND_PID; docker-compose down; exit" INT
wait
