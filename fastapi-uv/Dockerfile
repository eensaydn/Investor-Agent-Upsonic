# Python 3.11 slim image kullanıyoruz (hafif ve güvenli)
FROM python:3.11-slim

# Çalışma dizinini /app olarak ayarlıyoruz
WORKDIR /app

# Sistem paketlerini güncelle ve gerekli paketleri yükle
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıklarını kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Portları expose et (dışarıdan erişilebilir yap)
EXPOSE 8001 8501

# Varsayılan komut (container başladığında çalışacak)
CMD ["python", "start_project.py"]

