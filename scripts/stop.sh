#!/bin/bash

# Stop all services

echo "🛑 Stopping RAG Knowledge Base..."

# Stop backend
echo "Stopping backend..."
pkill -f "uvicorn app.main:app" || true

# Stop frontend
echo "Stopping frontend..."
pkill -f "react-scripts" || true

# Stop infrastructure
echo "Stopping infrastructure services..."
cd backend
docker-compose down

echo "✅ All services stopped!"
