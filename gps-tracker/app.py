
from fastapi import FastAPI
from kafka import KafkaProducer
import json

app = FastAPI(title="GPS Tracker Service")

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.post("/send-gps")
def send_gps():
    data = {"truck_id": 1, "lat": 52.5, "lon": 13.4}
    producer.send("gps", data)
    producer.flush()
    return {"status": "sent", "data": data}
