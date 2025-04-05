# GPS ETA Notifier (FastAPI + Kafka + Docker)

A simple educational microservices project where three services interact via Kafka.

## Architecture

```
gps-tracker (FastAPI)
   └──> Kafka Topic "gps"
         └──> eta-calculator (FastAPI)
                └──> Kafka Topic "eta"
                       └──> notifier (FastAPI)
```

## Quick Start (Local)

1. Clone the repository
2. Make sure Docker and Docker Compose are installed
3. Start everything:

```bash
docker compose up --build
```

## 🔗 Services Overview

| Service         | URL                        | Swagger UI           |
|-----------------|----------------------------|-----------------------|
| gps-tracker     | http://localhost:8000      | `/docs` (`/send-gps`) |
| eta-calculator  | http://localhost:8001      | `/docs` (`/calculate`) |
| notifier        | http://localhost:8002      | `/docs` (`/notify`)   |

## Stack

- Python 3.11
- FastAPI
- Apache Kafka + Zookeeper
- Docker & Docker Compose

## How to Test

1. Open Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
2. Trigger `/send-gps` in `gps-tracker`
3. ETA is calculated automatically by `eta-calculator`
4. `notifier` service will print the notification to console

## Shutdown

```bash
docker compose down
```

## Todo / Roadmap

- [ ] Push Docker images to Docker Hub
- [ ] Deploy to cloud (Kubernetes, Render, Railway, etc.)
- [ ] Add a frontend (React/Vue dashboard)

---

Built for learning Kafka, microservices, and container orchestration
