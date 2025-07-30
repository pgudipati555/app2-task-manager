# Task Management REST API - Complete Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture & Components](#architecture--components)
3. [Prerequisites](#prerequisites)
4. [Project Setup](#project-setup)
5. [Starting the Application](#starting-the-application)
6. [REST API Documentation](#rest-api-documentation)
7. [Testing the APIs](#testing-the-apis)
8. [Verification & Monitoring](#verification--monitoring)
9. [Stopping the Application](#stopping-the-application)
10. [Troubleshooting](#troubleshooting)
11. [Development Workflow](#development-workflow)

## Project Overview

The Task Management REST API is a containerized microservices application built for learning REST API concepts and Docker containerization. It provides a complete CRUD (Create, Read, Update, Delete) interface for managing tasks with persistent data storage.

**Learning Objectives:**
- Understand REST API principles and HTTP methods
- Learn Docker containerization and multi-service orchestration
- Practice database integration with APIs
- Experience Python client-server communication
- Master Docker Compose for development environments

## Architecture & Components

### System Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│   Python Client │◄──►│   Flask API     │◄──►│   PostgreSQL    │
│   (Port: N/A)   │    │   (Port: 5000)  │    │   (Port: 5432)  │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Component Details

#### 1. **Flask REST API Service (`api/`)**
- **Purpose**: Core REST API server handling HTTP requests
- **Technology**: Python Flask framework
- **Port**: 5000
- **Responsibilities**:
  - Handle HTTP requests (GET, POST, PUT, DELETE)
  - Validate input data and return appropriate status codes
  - Interact with PostgreSQL database
  - Return JSON responses
  - Provide health check endpoint

**Key Files:**
- `app.py`: Main Flask application with API endpoints
- `requirements.txt`: Python dependencies (Flask, psycopg2-binary)
- `Dockerfile`: Container configuration for API service

#### 2. **PostgreSQL Database Service (`database/`)**
- **Purpose**: Persistent data storage for tasks
- **Technology**: PostgreSQL 13
- **Port**: 5432
- **Responsibilities**:
  - Store task data with ACID compliance
  - Handle concurrent database operations
  - Maintain data integrity and relationships
  - Provide backup and recovery capabilities

**Key Files:**
- `init.sql`: Database schema and initial data setup

**Database Schema:**
```sql
tasks table:
├── id (SERIAL PRIMARY KEY)
├── title (VARCHAR(255) NOT NULL)
├── description (TEXT)
├── completed (BOOLEAN DEFAULT FALSE)
├── created_at (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
└── updated_at (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
```

#### 3. **Python Client Service (`client/`)**
- **Purpose**: Demonstrates API usage and testing
- **Technology**: Python with requests library
- **Responsibilities**:
  - Show examples of all REST operations
  - Test API connectivity and responses
  - Demonstrate proper error handling
  - Provide learning examples for API consumption

**Key Files:**
- `api_client.py`: Complete demo script showing all API operations
- `requirements.txt`: Python dependencies (requests)
- `Dockerfile`: Container configuration for client

#### 4. **Docker Compose Orchestration**
- **Purpose**: Coordinate multi-container application
- **Technology**: Docker Compose
- **Responsibilities**:
  - Define service dependencies
  - Configure network communication
  - Manage environment variables
  - Handle volume mounting and data persistence

## Prerequisites

### System Requirements
- **Docker**: Version 20.0 or higher
- **Docker Compose**: Version 2.0 or higher
- **Operating System**: Linux, macOS, or Windows with WSL2
- **Memory**: Minimum 2GB RAM available for Docker
- **Storage**: At least 1GB free disk space

### Installation Verification
```bash
# Check Docker installation
docker --version
docker-compose --version

# Verify Docker is running
docker ps
```

## Project Setup

### 1. Create Project Structure
```bash
mkdir task-manager-api && cd task-manager-api

# Create directory structure
mkdir -p api client database

# Create all necessary files as per the architecture
```

### 2. File Creation Checklist
- [ ] `docker-compose.yml` (root directory)
- [ ] `api/app.py`
- [ ] `api/requirements.txt`
- [ ] `api/Dockerfile`
- [ ] `client/api_client.py`
- [ ] `client/requirements.txt`
- [ ] `client/Dockerfile`
- [ ] `database/init.sql`

## Starting the Application

### Method 1: Complete Build and Start
```bash
# Navigate to project directory
cd task-manager-api

# Build and start all services
docker-compose up --build

# Expected output:
# ✅ Database initialization
# ✅ API service started on port 5000
# ✅ Client service ready
```

### Method 2: Detached Mode (Background)
```bash
# Start services in background
docker-compose up --build -d

# Check running containers
docker ps

# View logs
docker-compose logs -f
```

### Method 3: Individual Service Management
```bash
# Start only database
docker-compose up db

# Start API (requires database)
docker-compose up api

# Run client separately
docker-compose run client python api_client.py
```

### Startup Verification
1. **Database Ready**: Look for "database system is ready to accept connections"
2. **API Ready**: Look for "Running on http://0.0.0.0:5000"
3. **No Error Messages**: Ensure no connection errors or import failures

## REST API Documentation

### Base URL
```
http://localhost:5000/api
```

### Authentication
No authentication required (learning project)

### Content Type
All requests: `Content-Type: application/json`

### API Endpoints

#### 1. Health Check
- **Endpoint**: `GET /api/health`
- **Purpose**: Verify API service status
- **Response**: 200 OK
```json
{
  "status": "healthy",
  "timestamp": "2025-07-30T10:30:00.123456"
}
```

#### 2. Get All Tasks
- **Endpoint**: `GET /api/tasks`
- **Purpose**: Retrieve all tasks
- **Response**: 200 OK
```json
[
  {
    "id": 1,
    "title": "Sample Task 1",
    "description": "This is a sample task",
    "completed": false,
    "created_at": "2025-07-30T10:00:00",
    "updated_at": "2025-07-30T10:00:00"
  }
]
```

#### 3. Get Single Task
- **Endpoint**: `GET /api/tasks/{id}`
- **Purpose**: Retrieve specific task by ID
- **Response**: 200 OK (found) / 404 Not Found
```json
{
  "id": 1,
  "title": "Sample Task 1",
  "description": "This is a sample task",
  "completed": false,
  "created_at": "2025-07-30T10:00:00",
  "updated_at": "2025-07-30T10:00:00"
}
```

#### 4. Create New Task
- **Endpoint**: `POST /api/tasks`
- **Purpose**: Create a new task
- **Request Body**:
```json
{
  "title": "New Task",
  "description": "Task description",
  "completed": false
}
```
- **Response**: 201 Created
```json
{
  "id": 3,
  "title": "New Task",
  "description": "Task description",
  "completed": false,
  "created_at": "2025-07-30T10:30:00",
  "updated_at": "2025-07-30T10:30:00"
}
```

#### 5. Update Task
- **Endpoint**: `PUT /api/tasks/{id}`
- **Purpose**: Update existing task
- **Request Body** (partial updates allowed):
```json
{
  "title": "Updated Title",
  "description": "Updated description",
  "completed": true
}
```
- **Response**: 200 OK (updated) / 404 Not Found

#### 6. Delete Task
- **Endpoint**: `DELETE /api/tasks/{id}`
- **Purpose**: Delete specific task
- **Response**: 200 OK (deleted) / 404 Not Found
```json
{
  "message": "Task deleted successfully"
}
```

### HTTP Status Codes
- **200 OK**: Successful GET, PUT, DELETE
- **201 Created**: Successful POST
- **400 Bad Request**: Invalid request data
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

## Testing the APIs

### Method 1: Using the Python Client (Recommended)
```bash
# Run the automated demo
docker-compose run client python api_client.py

# Expected output: Complete demo of all API operations
```

### Method 2: Manual cURL Testing

#### Basic Health Check
```bash
curl http://localhost:5000/api/health
```

#### Get All Tasks
```bash
curl http://localhost:5000/api/tasks
```

#### Create a New Task
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn Docker",
    "description": "Complete Docker tutorial",
    "completed": false
  }'
```

#### Get Specific Task
```bash
curl http://localhost:5000/api/tasks/1
```

#### Update Task
```bash
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Docker tutorial completed!",
    "completed": true
  }'
```

#### Delete Task
```bash
curl -X DELETE http://localhost:5000/api/tasks/1
```

### Method 3: Using Postman or Similar Tools
1. Import the API endpoints into Postman
2. Set base URL: `http://localhost:5000/api`
3. Test each endpoint with appropriate HTTP methods
4. Verify response codes and data

### Method 4: Browser Testing (GET only)
- Open browser and navigate to:
  - `http://localhost:5000/api/health`
  - `http://localhost:5000/api/tasks`
  - `http://localhost:5000/api/tasks/1`

## Verification & Monitoring

### 1. Container Health Verification
```bash
# Check all running containers
docker ps

# Verify specific container logs
docker-compose logs api
docker-compose logs db
docker-compose logs client

# Check container resource usage
docker stats
```

### 2. Database Verification
```bash
# Connect to PostgreSQL database
docker-compose exec db psql -U taskuser -d taskdb

# Run SQL queries
SELECT * FROM tasks;
SELECT COUNT(*) FROM tasks;
\dt  # List tables
\q   # Exit
```

### 3. API Response Verification
```bash
# Test with verbose output
curl -v http://localhost:5000/api/health

# Test error handling
curl http://localhost:5000/api/tasks/999

# Test invalid data
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"invalid": "data"}'
```

### 4. Network Connectivity
```bash
# Check Docker networks
docker network ls

# Inspect project network
docker network inspect task-manager-api_default

# Test inter-container communication
docker-compose exec client ping api
docker-compose exec api ping db
```

### 5. Performance Testing
```bash
# Simple load test with curl
for i in {1..10}; do
  curl -s http://localhost:5000/api/health > /dev/null &
done
wait

# Check API response times
time curl http://localhost:5000/api/tasks
```

## Stopping the Application

### Method 1: Graceful Shutdown
```bash
# Stop all services (keeps data)
docker-compose down

# Verify containers stopped
docker ps
```

### Method 2: Complete Cleanup
```bash
# Stop and remove containers + networks
docker-compose down

# Remove volumes (deletes database data)
docker-compose down -v

# Remove images (optional)
docker-compose down --rmi all

# Complete system cleanup
docker system prune -a
```

### Method 3: Individual Service Control
```bash
# Stop specific service
docker-compose stop api
docker-compose stop db

# Start specific service
docker-compose start api
```

### Method 4: Force Stop
```bash
# If services don't respond to normal shutdown
docker-compose kill

# Clean up remaining containers
docker container prune
```

## Troubleshooting

### Common Issues and Solutions

#### 1. SSL Certificate Errors During Build
**Problem**: SSL certificate verification failed
**Solution**: Already implemented in Dockerfiles with `--trusted-host` flags

#### 2. Port Already in Use
**Problem**: Port 5000 or 5432 already occupied
```bash
# Find process using port
sudo lsof -i :5000
sudo lsof -i :5432

# Kill process or change ports in docker-compose.yml
```

#### 3. Database Connection Issues
**Problem**: API can't connect to database
```bash
# Check database logs
docker-compose logs db

# Verify database is ready
docker-compose exec db pg_isready -U taskuser

# Test connection manually
docker-compose exec db psql -U taskuser -d taskdb -c "SELECT 1;"
```

#### 4. API Not Responding
**Problem**: API endpoints return errors
```bash
# Check API logs
docker-compose logs api

# Verify API container is running
docker ps | grep api

# Test internal connectivity
docker-compose exec client curl http://api:5000/api/health
```

#### 5. Python Import Errors
**Problem**: Missing dependencies or import failures
```bash
# Rebuild containers
docker-compose build --no-cache

# Check requirements.txt files
# Verify all dependencies are listed
```

#### 6. Data Persistence Issues
**Problem**: Data disappears after restart
```bash
# Check volume configuration
docker volume ls
docker volume inspect task-manager-api_postgres_data

# Ensure volumes are properly mounted in docker-compose.yml
```

### Debug Commands
```bash
# Interactive shell in containers
docker-compose exec api bash
docker-compose exec db bash
docker-compose exec client bash

# View detailed container information
docker inspect container_name

# Monitor real-time logs
docker-compose logs -f --tail=100

# Check environment variables
docker-compose exec api env
```

## Development Workflow

### Making Changes

#### 1. Code Changes
```bash
# Make changes to source files
# Restart specific service
docker-compose restart api

# Or rebuild if requirements changed
docker-compose up --build api
```

#### 2. Database Schema Changes
```bash
# Stop services
docker-compose down

# Remove database volume
docker-compose down -v

# Update init.sql
# Restart (will recreate database)
docker-compose up --build
```

#### 3. Testing New Features
```bash
# Create test branch
git checkout -b feature/new-endpoint

# Make changes and test
docker-compose up --build

# Run client tests
docker-compose run client python api_client.py
```

### Best Practices

1. **Always use version control**
2. **Test changes in isolated containers**
3. **Monitor logs during development**
4. **Use docker-compose for consistent environments**
5. **Clean up unused containers and images regularly**
6. **Document API changes**
7. **Test error scenarios**

### Extensions and Learning Exercises

1. **Add Authentication**
   - Implement JWT tokens
   - Add user management

2. **Add Validation**
   - Input validation middleware
   - Schema validation

3. **Add Monitoring**
   - Health check endpoints
   - Logging middleware
   - Metrics collection

4. **Performance Optimization**
   - Database indexing
   - Connection pooling
   - Caching layers

5. **Testing Framework**
   - Unit tests for API endpoints
   - Integration tests
   - Load testing

---

## Quick Reference

### Essential Commands
```bash
# Start everything
docker-compose up --build

# Test API
docker-compose run client python api_client.py

# View logs
docker-compose logs -f

# Stop everything
docker-compose down

# Complete cleanup
docker-compose down -v && docker system prune -a
```

### API Quick Test
```bash
curl http://localhost:5000/api/health
curl http://localhost:5000/api/tasks
```

### Emergency Stop
```bash
docker-compose kill
docker container prune -f
```

This documentation provides a comprehensive guide for understanding, deploying, testing, and maintaining the Task Management REST API application. Each section is designed to be self-contained while building upon previous concepts for effective learning.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review the logs using `docker-compose logs`
3. Open an issue in the GitHub repository

## Acknowledgments

- Built for learning REST API concepts and Docker containerization
- Uses Flask for the REST API framework
- PostgreSQL for reliable data persistence
- Docker and Docker Compose for containerization