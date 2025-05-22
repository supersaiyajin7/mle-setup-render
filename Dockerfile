# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# System deps, install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app + test code
COPY app/ app/
COPY tests/ tests/

# Add this to make 'app' importable
ENV PYTHONPATH=/app

# Run tests
RUN pytest tests/

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
