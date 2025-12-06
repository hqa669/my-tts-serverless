# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY handler.py /app/handler.py

# Install any dependencies if needed; for echo example, none.
# RUN pip install ...

# Run a simple WSGI server — Runpod expects your container to listen on an HTTP port:
# For simplicity, use an extremely minimal Flask app that wraps the handler.
RUN pip install flask

COPY run_server.py /app/run_server.py

EXPOSE 80
CMD ["python", "run_server.py"]

