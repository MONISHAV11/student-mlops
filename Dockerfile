# Use official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY app/ app/
COPY src/ src/

# Optional: environment variable to make Python output unbuffered
ENV PYTHONUNBUFFERED=1

# Default command: run your main.py
CMD ["python", "-m", "app.main"]
