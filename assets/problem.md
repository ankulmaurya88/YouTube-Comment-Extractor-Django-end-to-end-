# 📘 Project 1: YouTube Comment Extraction Service

---

## 🚀 Overview

The **YouTube Comment Extraction Service** is a scalable backend system designed to fetch, process, and analyze comments from public YouTube videos using the YouTube Data API v3.

The system is built with a production-oriented architecture focusing on asynchronous processing, background task execution, caching, and database indexing to handle large-scale comment ingestion efficiently.

---

## 🎯 Problem Statement

Modern analysts, researchers, and digital marketers require structured access to YouTube comments for:

- Sentiment analysis  
- Engagement monitoring  
- Audience behavior insights  

However, existing approaches often suffer from:

- Synchronous and blocking API calls  
- Poor scalability for large comment volumes  
- Lack of retry handling for API quota limits  
- No structured storage for querying  
- Repeated API calls due to missing caching  
- No background job processing  
- Limited observability and monitoring  

This project addresses these limitations by designing a production-ready ingestion system with asynchronous processing and scalable architecture.

---

## 🏗 Architecture Overview

```
Client (React/Vite)
        ↓
FastAPI (Async API Layer)
        ↓
Redis (Caching + Rate Limiting)
        ↓
Celery Worker (Background Processing)
        ↓
YouTube Data API
        ↓
PostgreSQL (Persistent Storage)
```

---

## 🔥 Key Features

### ✅ Asynchronous API Layer

- Built using FastAPI  
- Non-blocking request handling  
- Supports high concurrency  

### ✅ Background Task Processing

- Celery-based job execution  
- Non-blocking comment ingestion  
- Retry with exponential backoff  

### ✅ Structured Storage

- PostgreSQL for persistent storage  
- Indexed by `video_id` and `published_at`  
- Supports paginated queries  

### ✅ Caching Layer

- Redis-based caching  
- Reduces repeated YouTube API calls  
- Improves latency  

### ✅ Rate Limiting

- Prevents API abuse  
- Protects against quota exhaustion  

### ✅ Observability

- Structured JSON logging  
- Health check endpoints  
- Error categorization  

---

## 📦 API Endpoints

### 1️⃣ Fetch Comments

**POST** `/api/v1/comments/fetch`

#### Request

```json
{
  "video_id": "string",
  "max_results": 200
}
```

#### Response

```json
{
  "success": true,
  "task_id": "uuid"
}
```

---

### 2️⃣ Check Job Status

**GET** `/api/v1/comments/status/{task_id}`

---

### 3️⃣ Get Comments (Paginated)

**GET** `/api/v1/comments/{video_id}?page=1&limit=20`

---

## 🧠 Engineering Concepts Applied

- Asyncio event loop  
- Background job queues  
- GIL-aware architecture (CPU vs I/O separation)  
- Database indexing  
- Caching strategies  
- API rate control  
- Containerized deployment  

---

## 🐳 Deployment

- Dockerized backend  
- Gunicorn + Uvicorn workers  
- Redis and PostgreSQL via Docker Compose  
- CI/CD ready  

---

## 📊 Scalability Strategy

- Horizontal scaling of FastAPI instances  
- Independent scaling of Celery workers  
- Redis shared across services  
- Read replicas for PostgreSQL (future enhancement)  

---

## 🔮 Future Enhancements

- Sentiment analysis via multiprocessing  
- Keyword extraction  
- Real-time dashboard analytics  
- Prometheus metrics integration  
- Kubernetes deployment  
