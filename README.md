# Salesforce CRM Data Pipeline

Data integration with Salesforce Data Cloud and a user interface to perform and view operations

## Table of Contents
- [Overview](#overview)
- [Objective](#objective)
- [Technologies Used](#technologies-used)
- [Key Features](#key-features)
- [Setup Instructions](#setup-instructions)
- [Folder Structure](#folder-structure)
- [Future Enhancements](#future-enhancements)

## Overview

The Salesforce CRM Data Pipeline project automates the extraction, transformation, and loading (ETL) of Salesforce CRM data into PostgreSQL and MongoDB databases. The project uses Kafka for event-driven architecture and integrates with a Flask-based UI dashboard for managing and visualizing the data pipeline

## Objective

To develop an efficient data pipeline that:
- Automates the ETL process for Salesforce CRM data
- Provides real-time data streaming and processing using Kafka
- Visualizes data through an interactive UI dashboard
- Supports decision-making by integrating structured (PostgreSQL) and unstructured (MongoDB) data storage

## Technologies Used
- **Airflow**: Orchestrates the ETL workflow
- **Kafka**: Event streaming platform to handle data integration events
- **PostgreSQL**: Relational database for structured data
- **MongoDB**: NoSQL database for unstructured data
- **Flask**: Web framework for building the dashboard and authentication system
- **SQLAlchemy**: ORM for PostgreSQL database integration
- **Docker**: Containerization of the application for easy deployment and scalability
- **Python**: Backend programming language
- **PyYAML**: For loading environment configurations from YAML files

## Key Features

### 1. End-to-End ETL Pipeline
- Extract data from various sources
- Transform data to match organizational requirements
- Load data into Salesforce Data Cloud

### 2. Real-Time Data Streaming
- Kafka-based architecture ensures timely data integration and processing

### 3. User Interface Dashboard
- Manage pipeline configurations
- Monitor the status of data jobs
- Visualize data insights with user-friendly charts and tables

### 4. Database Integration
- PostgreSQL for structured data storage (e.g., customer records, transactions)
- MongoDB for unstructured data (e.g., logs, metadata)

## Setup Instructions

### Prerequisites
- Python 3.9+
- Docker and Docker Compose
- PostgreSQL and MongoDB (if not using Docker containers)
- Flask and necessary Python libraries

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Salesforce_CRM_DataPipeline.git
    cd Salesforce_CRM_DataPipeline
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a .env file in the root directory with the following content:
    ```dotenv
    # Database configurations
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=admin
    DB_PASSWORD=admin
    DB_NAME=sf_data_integration

    # Kafka configurations
    KAFKA_BROKER_URL=kafka:9092
    DATA_INTEGRATION_TOPIC=data_integration_events

    # Salesforce configurations
    SALESFORCE_API_URL=https://api.salesforce.com
    SALESFORCE_CLIENT_ID=your-client-id
    SALESFORCE_CLIENT_SECRET=your-client-secret
    SALESFORCE_USERNAME=your-username
    SALESFORCE_PASSWORD=your-password

    # UI Dashboard
    FLASK_APP=ui_dashboard.app
    FLASK_ENV=development
    SECRET_KEY=supersecretkey
    ```

### Running the Application

1. **Run Docker Containers:**
    ```bash
    docker-compose up --build
    ```
    This will start:
    - PostgreSQL
    - MongoDB
    - Kafka
    - Airflow (if needed)
    - The Flask app (UI Dashboard)

2. **Run Flask Application:**
    ```bash
    flask run
    ```
    You can now access:
    - UI dashboard at http://localhost:5000
    - Airflow UI at http://localhost:8080

## Folder Structure
```plaintext
Salesforce_CRM_DataPipeline/
│
├── airflow_dags/           # Airflow DAGs for ETL pipeline
├── cli_backend/            # Backend logic for connectors and data processing
│   ├── __init__.py
│   ├── requirements.txt
│   └── setup.py
│
├── config/                 # Configuration files for different environments
│   ├── __init__.py
│   ├── base.yaml
│   ├── development.yaml
│   └── production.yaml
│
├── databases/              # Initialization scripts for MongoDB and PostgreSQL
├── docker/                 # Docker configuration files
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── examples/               # Example integration scripts
├── kafka/                  # Kafka producer and consumer scripts
├── ui_dashboard/           # Flask-based UI dashboard
│   ├── __init__.py
│   ├── app.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── routes.py
│   ├── dashboard/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── routes.py
│   └── templates/
│       ├── base.html
│       └── dashboard.html
│
└── requirements.txt
```

## Future Enhancements
1. Integrate machine learning models for predictive analytics
2. Implement enhanced monitoring and alerting for the pipeline
3. Support multi-region deployments using cloud services
