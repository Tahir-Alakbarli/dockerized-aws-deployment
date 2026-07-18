FROM python:3.12-slim

WORKDIR /app

COPY server.py .
COPY frontend ./frontend

EXPOSE 8000

CMD ["python", "server.py"]
