# Salesforce_crm_pipeline
- Data integration with salesforce data cloud and a user interface to perform and view operations.

## Technologies Used
- Flask: Web framework for building the dashboard and authentication system
- SQLAlchemy: ORM for PostgreSQL database integration
- PostgreSQL: Relational database used for storing structured data
- MongoDB: NoSQL database for unstructured data
- Kafka: Event streaming platform to handle data integration events
- Docker: Containerization of the application
- Python: Backend programming language
- PyYAML: For loading environment configurations from YAML files

## Pre-requisite
### Environment Setup
- Python 3.9+
- Docker and Docker Compose
- PostgreSQL and MongoDB (if not using Docker containers)
- Flask and necessary Python libraries

### Installation Steps
- Clone the repository:
  - *git clone https://github.com/yourusername/sf_data_integration_project.git*
  - *cd sf_data_integration_project*
- Create and activate virtual environment:
  - *python3 -m venv venv*
  - *source venv/bin/activate* # On Windows, use `venv\Scripts\activate`
- Install dependencies:
  - *pip install -r requirements.txt*

### Configuration Setup
- Create .env file in root directory with following content:
  - DB_HOST=localhost
  - DB_PORT=5432
  - DB_USER=admin
  - DB_PASSWORD=admin
  - DB_NAME=sf_data_integration
  - KAFKA_BROKER_URL=kafka:9092
  - DATA_INTEGRATION_TOPIC=data_integration_events
  - SALESFORCE_API_URL=https://api.salesforce.com
  - SALESFORCE_CLIENT_ID=your-client-id
  - SALESFORCE_CLIENT_SECRET=your-client-secret
  - SALESFORCE_USERNAME=your-username
  - SALESFORCE_PASSWORD=your-password
  - FLASK_APP=ui_dashboard.app
  - FLASK_ENV=development
  - SECRET_KEY=supersecretkey

## Running Application
- Run with Docker:
  - *docker-compose up --build*
  - This starts PostgreSQL, MongoDB, Kafka, and Flask app
- Run Flask separately:
  - *flask run*
  - Access dashboard at http://localhost:5000

## Project Structure
- config/
  - base.yaml
  - development.yaml
  - production.yaml
- cli_backend/
  - requirements.txt
  - setup.py
- ui_dashboard/
  - app.py
  - auth/
  - dashboard/
  - templates/
- docker/
  - Dockerfile
  - docker-compose.yml
- requirements.txt

## Contributing
- Submit issues and pull requests
- Follow established code style
- Ensure changes pass existing tests
