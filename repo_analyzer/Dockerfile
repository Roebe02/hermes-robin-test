FROM python:3.11-slim

WORKDIR /app

# Install git (für git clone)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY cli.py .
COPY app.py .
COPY index.html .
COPY setup.py .

# Expose port
EXPOSE 8000

# Run
CMD ["python", "app.py"]
