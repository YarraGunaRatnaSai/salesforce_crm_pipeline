import pytest
from cli_backend.integrators.salesforce_integrator import SalesforceIntegrator
from cli_backend.connectors.salesforce_connector import SalesforceConnector
from cli_backend.connectors.database_connector import DatabaseConnector

def test_salesforce_integrator_execution():
    """
    Test the execution of the SalesforceIntegrator.
    """
    source_connector = SalesforceConnector(username="test_user", password="test_pass", token="test_token")
    target_connector = DatabaseConnector(db_type="postgres", config={"dbname": "test_db"})
    integrator = SalesforceIntegrator(source_connector, target_connector)

    # Mocking the methods
    integrator.extract = lambda: [{"name": "Alice", "age": 25}]
    integrator.transform = lambda data: [{"name": "Alice", "age": 30}]
    integrator.load = lambda data: True

    integrator.execute()
