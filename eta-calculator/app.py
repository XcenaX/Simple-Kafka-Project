
from fastapi import FastAPI, Body
from kafka import KafkaConsumer, KafkaProducer
import threading, json, random

app = FastAPI(title="ETA Calculator Service")

consumer = KafkaConsumer(
    'gps',
    bootstrap_servers='kafka:9092',
    group_id='eta-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def calculate_eta(gps: dict) -> dict:
    eta = {
        "truck_id": gps["truck_id"],
        "eta_minutes": random.randint(10, 60)
    }
    print("🧮 Calculated ETA:", eta)
    return eta

@app.post("/calculate")
def manual_trigger(gps: dict = Body(...)):
    eta = calculate_eta(gps)
    producer.send("eta", eta)
    producer.flush()
    return {"status": "calculated", "eta": eta}

def consume():
    for msg in consumer:
        gps = msg.value
        eta = calculate_eta(gps)
        producer.send("eta", eta)
        producer.flush()

@app.on_event("startup")
def start_consumer():
    threading.Thread(target=consume, daemon=True).start()
