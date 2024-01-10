# salesforce_integration_dashboard
Data integration with salesforce data cloud and a user interface to perform and view operationa
=======
# SF Data Integration Project

This project integrates Salesforce data with a PostgreSQL and MongoDB backend, utilizing Kafka for event-driven architecture. It includes a Flask-based UI dashboard for user authentication and interaction with the integration processes.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project is designed to facilitate the integration of Salesforce data into a backend architecture with PostgreSQL and MongoDB databases. It uses Kafka for managing data integration events. The application includes an authentication system, a dashboard for data visualization, and an admin interface.

## Technologies Used

- **Flask**: Web framework for building the dashboard and authentication system.
- **SQLAlchemy**: ORM for PostgreSQL database integration.
- **PostgreSQL**: Relational database used for storing structured data.
- **MongoDB**: NoSQL database for unstructured data.
- **Kafka**: Event streaming platform to handle data integration events.
- **Docker**: Containerization of the application for easy deployment and scalability.
- **Python**: Backend programming language.
- **PyYAML**: For loading environment configurations from YAML files.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.9+
- Docker and Docker Compose
- PostgreSQL and MongoDB (if not using Docker containers)
- Flask and necessary Python libraries

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/sf_data_integration_project.git
   cd sf_data_integration_project
   ```

2. **Create and activate a virtual environment:**
   '''bash
   python3 -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   '''

3. **Install dependencies:**
   Install the required Python packages:
   '''bash
   pip install -r requirements.txt
   '''

4. **Set up environment variables:**
   Create a .env file in the root directory with the following content:
   '''dotenv

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
   '''

### Running the Application

1. **Run Docker Containers:**
   If you want to run the application with Docker, use the following command to start all services:
   '''bash
   docker-compose up --build
   '''
   This will start:
   PostgreSQL
   MongoDB
   Kafka
   Airflow (if needed)
   The Flask app (UI Dashboard)

2. **Run Flask Application:**
   If you're running the Flask app outside Docker, use:
   '''bash
   flask run
   '''
   You can now access the UI dashboard at http://localhost:5000.

## Configuration

The configuration files are located in the config/ directory, where environment-specific settings (e.g., development.yaml, production.yaml) are stored.

### Environment Variables

The following environment variables can be configured:
DB_HOST: Host for the PostgreSQL database.
DB_PORT: Port for PostgreSQL.
DB_USER: Username for PostgreSQL.
DB_PASSWORD: Password for PostgreSQL.
DB_NAME: Name of the PostgreSQL database.
KAFKA_BROKER_URL: URL for the Kafka broker.
DATA_INTEGRATION_TOPIC: Kafka topic for data events.
SALESFORCE_API_URL: Salesforce API URL.
SALESFORCE_CLIENT_ID: Salesforce client ID.
SALESFORCE_CLIENT_SECRET: Salesforce client secret.
SALESFORCE_USERNAME: Salesforce username.
SALESFORCE_PASSWORD: Salesforce password.
FLASK_APP: Flask app entry point.
FLASK_ENV: Flask environment (development, production).
SECRET_KEY: Secret key for Flask sessions.

### Folder Structure

'''plaintext
sf_data_integration_project/
│
├── config/
│ ├── **\_init**.py
│ ├── base.yaml
│ ├── development.yaml
│ └── production.yaml
│
├── cli_backend/
│ ├── **init**.py
│ ├── requirements.txt
│ └── setup.py
│
├── ui_dashboard/
│ ├── **init**.py
│ ├── app.py
│ ├── auth/
│ │ ├── **init**.py
│ │ ├── models.py
│ │ └── routes.py
│ ├── dashboard/
│ │ ├── **init**.py
│ │ ├── helpers.py
│ │ └── routes.py
│ └── templates/
│ ├── base.html
│ └── dashboard.html
│
├── docker/
│ ├── Dockerfile
│ └── docker-compose.yml
│
└── requirements.txt
'''

## Contributing

Feel free to submit issues and pull requests. When contributing, please follow the established code style and ensure your changes pass existing tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
>>>>>>> a88209f (Initial Commit)
