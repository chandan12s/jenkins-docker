FROM python:3.11-slim

WORKDIR /app

# Copy application
COPY app.py /app/app.py

RUN chmod +x /app/app.py

ENTRYPOINT ["python", "app.py"]
