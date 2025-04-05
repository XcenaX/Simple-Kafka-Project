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
3. Start everything locally:

```bash
docker compose up --build
```

## Services Overview

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

## How to Test Locally

1. Open Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
2. Trigger `/send-gps` in `gps-tracker`
3. ETA is calculated automatically by `eta-calculator`
4. `notifier` service will print the notification to console

## Shutdown

```bash
docker compose down
```

## Deploying to Production

To deploy using Render and `render.yaml`:

1. Replace `xcenax` in Docker image names with **your Docker Hub username**
2. Replace the GitHub repo URL in `render.yaml` with **your own GitHub repo**, for example:

```yaml
repo: https://github.com/yourusername/your-repo-name
```

3. Push Docker images to Docker Hub:

```bash
docker build -t yourusername/gps-tracker:latest ./gps-tracker
docker push yourusername/gps-tracker:latest
# Repeat for eta-calculator and notifier
```

4. Commit and push `render.yaml` to your GitHub repo
5. Go to [https://render.com](https://render.com), click **New + → Blueprint**
6. Select your repo and Render will deploy everything

---

Built for learning Kafka, microservices, and container orchestration 🚀
