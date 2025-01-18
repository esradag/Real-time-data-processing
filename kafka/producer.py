import sys
import os

# Python modül yolunu ayarla
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from kafka import KafkaProducer
import json
import time
from utils.coingecko_api import fetch_crypto_data



producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = fetch_crypto_data()
    producer.send('crypto-topic', data)
    print("Veri Kafka'ya gönderildi:", data)
    time.sleep(60)
