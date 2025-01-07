import pytest
from cli_backend.connectors.salesforce_connector import SalesforceConnector
from cli_backend.connectors.database_connector import DatabaseConnector

def test_salesforce_connector_initialization():
    """
    Test initialization of SalesforceConnector.
    """
    connector = SalesforceConnector(username="test_user", password="test_pass", token="test_token")
    assert connector.username == "test_user"

def test_database_connector_initialization():
    """
    Test initialization of DatabaseConnector.
    """
    config = {"dbname": "test_db", "user": "test_user", "password": "test_pass", "host": "localhost", "port": 5432}
    connector = DatabaseConnector(db_type="postgres", config=config)
    assert connector.db_type == "postgres"
