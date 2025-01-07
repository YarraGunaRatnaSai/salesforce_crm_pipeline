# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r cli_backend/requirements.txt
RUN pip install --no-cache-dir -r ui_dashboard/requirements.txt

# Set environment variables
ENV FLASK_APP=ui_dashboard/app.py

# Expose ports for Flask and Airflow
EXPOSE 5000 8080

# Start both the CLI backend and Flask UI
CMD ["sh", "-c", "python cli_backend/setup.py && flask run --host=0.0.0.0"]
