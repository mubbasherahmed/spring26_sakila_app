FROM python:3.9-slim
LABEL maintainer="Mubbasher-Ahmed" version="1.0" description="Optimized Sakila App"
WORKDIR /app
RUN useradd -m sakilauser && apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chown -R sakilauser:sakilauser /app
USER sakilauser
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s CMD wget --quiet --spider http://localhost:5000/ || exit 1
CMD ["python", "app.py"]