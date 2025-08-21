# # Use official Python image
# FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Set working directory
# WORKDIR /app

# # Install dependencies
# COPY requirements.txt .
# RUN pip install --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt

# # Copy project files
# COPY . .

# # Expose port
# EXPOSE 8000

# # Run Django with Gunicorn
# CMD ["gunicorn", "web.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]


# Use official Python 3.10 slim image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies for some Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files
COPY . .

# Expose the port Gunicorn will run on
EXPOSE 8000

# Run Django app with Gunicorn
CMD ["gunicorn", "web.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
