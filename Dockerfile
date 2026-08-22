FROM mcr.microsoft.com/playwright/python:v1.62.0

WORKDIR /app

# Copy dependency specifications
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project source code
COPY . .

# Environment variables setup
ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
