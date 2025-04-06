
from fastapi import FastAPI, Body
from kafka import KafkaConsumer
import threading, json, os

app = FastAPI(root_path="/notify")

consumer = KafkaConsumer(
    'eta',
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092"),
    group_id='notifier-group',
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

def notify(eta):
    print(f"Truck {eta['truck_id']} will arrive in {eta['eta_minutes']} minutes.")

@app.post("/notify")
def manual(eta: dict = Body(...)):
    notify(eta)
    return {"notified": eta}

def consume():
    for msg in consumer:
        notify(msg.value)

@app.on_event("startup")
def start():
    threading.Thread(target=consume, daemon=True).start()
