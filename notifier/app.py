
from fastapi import FastAPI, Body
from kafka import KafkaConsumer
import threading, json

app = FastAPI(title="Notifier Service")

consumer = KafkaConsumer(
    'eta',
    bootstrap_servers='kafka:9092',
    group_id='notifier-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def notify(eta: dict):
    print(f"🔔 Notification: Truck {eta['truck_id']} arriving in {eta['eta_minutes']} minutes.")

@app.post("/notify")
def manual_trigger(eta: dict = Body(...)):
    notify(eta)
    return {"status": "notified", "eta": eta}

def consume():
    for msg in consumer:
        eta = msg.value
        notify(eta)

@app.on_event("startup")
def start_consumer():
    threading.Thread(target=consume, daemon=True).start()
