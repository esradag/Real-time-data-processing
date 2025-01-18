FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kafka, utils ve tüm proje dosyalarını kopyala
COPY . /app

# Kafka Producer'ı başlat
CMD ["python", "kafka/producer.py"]
