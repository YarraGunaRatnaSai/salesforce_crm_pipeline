from sf_data_integration.connectors.salesforce_connector import SalesforceConnector
from sf_data_integration.connectors.database_connector import DatabaseConnector
from sf_data_integration.core.data_mapper import DataMapper
from sf_data_integration.utils.logging import setup_logger

# Setup logging
logger = setup_logger('integration_example', log_dir='sf_data_integration/logs')

# Initialize connectors
salesforce_connector = SalesforceConnector({
    'username': 'user@example.com',
    'password': 'password',
    'security_token': 'security_token'
})
salesforce_connector.connect()

database_connector = DatabaseConnector({
    'dbname': 'salesforce_data',
    'user': 'db_user',
    'password': 'db_password',
    'host': 'localhost',
    'port': 5432
})
database_connector.connect()

# Fetch data from Salesforce
salesforce_data = salesforce_connector.fetch_data("SELECT Id, Name FROM Contact LIMIT 10")
logger.info(f"Salesforce Data: {salesforce_data}")

# Map the data
data_mapper = DataMapper(mapping={"Id": "ContactId", "Name": "ContactName"})
mapped_data = data_mapper.apply_mapping(salesforce_data)

# Push data to the database
database_connector.push_data(mapped_data, 'contact_table')
logger.info(f"Pushed {len(mapped_data)} records to the database.")
