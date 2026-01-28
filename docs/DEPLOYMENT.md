# Deployment Guide

## Production Deployment

### Environment Variables

Create a `.env` file in the backend directory:

```bash
# Production settings
DEBUG=False
SECRET_KEY=your-secure-secret-key

# Database
DATABASE_URL=postgresql+asyncpg://user:password@db-host:5432/ragops

# MinIO
MINIO_ENDPOINT=minio-host:9000
MINIO_ACCESS_KEY=your-access-key
MINIO_SECRET_KEY=your-secret-key
MINIO_SECURE=True

# ChromaDB
CHROMA_HOST=chroma-host
CHROMA_PORT=8000

# Ollama
OLLAMA_HOST=http://ollama-host:11434

# CORS
ALLOWED_ORIGINS=https://yourdomain.com
```

### Docker Deployment

1. **Build Docker images:**
```bash
docker build -t ragops-backend ./backend
docker build -t ragops-frontend ./frontend
```

2. **Run with Docker Compose:**
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Cloud Deployment

#### AWS

1. **ECS/Fargate:**
   - Deploy backend as ECS service
   - Use RDS for PostgreSQL
   - Use S3 instead of MinIO
   - Deploy ChromaDB on ECS
   - Deploy Ollama on GPU-enabled instance

2. **Environment:**
   - Use AWS Secrets Manager for credentials
   - Use ALB for load balancing
   - Configure Auto Scaling

#### Google Cloud Platform

1. **Cloud Run:**
   - Deploy backend on Cloud Run
   - Use Cloud SQL for PostgreSQL
   - Use Cloud Storage instead of MinIO
   - Deploy ChromaDB on GKE

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ragops-backend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ragops-backend
  template:
    metadata:
      labels:
        app: ragops-backend
    spec:
      containers:
      - name: backend
        image: ragops-backend:latest
        ports:
        - containerPort: 8080
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: ragops-secrets
              key: database-url
```

### Security Checklist

- [ ] Use HTTPS in production
- [ ] Set strong SECRET_KEY
- [ ] Use environment variables for credentials
- [ ] Enable CORS only for trusted origins
- [ ] Use database connection pooling
- [ ] Implement rate limiting
- [ ] Set up monitoring and logging
- [ ] Regular security updates
- [ ] Backup strategy for databases

### Monitoring

1. **Application Metrics:**
   - Response times
   - Error rates
   - Request volume

2. **Infrastructure Metrics:**
   - CPU/Memory usage
   - Database connections
   - Storage usage

3. **Logging:**
   - Centralized logging (ELK Stack, CloudWatch)
   - Error tracking (Sentry)
   - Audit logs

### Backup Strategy

1. **Database:**
   - Automated daily backups
   - Backup retention policy
   - Test restore procedures

2. **Object Storage:**
   - Versioning enabled
   - Cross-region replication
   - Lifecycle policies

### Scaling

1. **Horizontal Scaling:**
   - Multiple backend instances
   - Load balancer
   - Session management

2. **Vertical Scaling:**
   - Increase instance sizes
   - Optimize database queries
   - Cache frequently accessed data
