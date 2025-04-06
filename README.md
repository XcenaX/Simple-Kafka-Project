# Simple Kafka Microservices with FastAPI + Kubernetes

This project is a demonstration of an event-driven architecture using **FastAPI**, **Apache Kafka**, and **Kubernetes (Minikube)**.

---

## Microservices

| Service         | Description                          | Kafka Topic |
|----------------|--------------------------------------|-------------|
| `gps-tracker`  | Sends GPS location events            | `gps`       |
| `eta-calculator` | Calculates ETA from GPS             | `eta`       |
| `notifier`     | Receives ETA and logs notification   | –           |

---

## Stack

- Python + FastAPI
- Kafka + Zookeeper (Bitnami)
- Docker & Docker Hub
- Kubernetes via Minikube
- Ingress + Swagger UI

---

## Endpoints (via Ingress)

| URL                          | Service         |
|-----------------------------|-----------------|
| `http://gps.local/gps/docs` | `gps-tracker`   |
| `http://gps.local/eta/docs` | `eta-calculator`|
| `http://gps.local/notify/docs` | `notifier`     |

> ℹ️ Add `gps.local` etc. to your `/etc/hosts` mapped to `minikube ip`

```
192.168.xx.xx gps.local
192.168.xx.xx eta.local
192.168.xx.xx notify.local
```

---

## How to Run (Minikube)

1. Enable ingress:
```bash
minikube addons enable ingress
```

2. Apply manifests:
```bash
kubectl apply -f zookeeper.yaml
kubectl apply -f kafka.yaml
kubectl apply -f gps-tracker-deployment.yaml
kubectl apply -f eta-calculator-deployment.yaml
kubectl apply -f notifier-deployment.yaml
kubectl apply -f ingress.yaml
```

3. Add `hosts` entries using `minikube ip`.

4. Open Swagger and test:
- POST `/send-gps` → triggers GPS event
- ETA gets calculated and forwarded
- Notifier logs ETA

---

## Docker Images

Images are hosted on Docker Hub under:

```
xcenax/gps-tracker
xcenax/eta-calculator
xcenax/notifier
```

> Replace `xcenax` with your Docker Hub username if you fork this repo.

---

## Credits

Built with ❤️ and caffeine by a true Kubernetes Enjoyer.