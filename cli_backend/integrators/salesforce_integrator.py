import pandas as pd
from .base_integrator import BaseIntegrator

class SalesforceIntegrator(BaseIntegrator):
    """
    Integrator for Salesforce ETL processes.
    """
    def extract(self):
        """
        Extract data from Salesforce.
        """
        try:
            data = self.source_connector.connection.query_all("SELECT * FROM Account")
            records = pd.DataFrame(data["records"])
            print(f"Extracted {len(records)} records from Salesforce.")
            return records
        except Exception as e:
            raise RuntimeError(f"Failed to extract data: {e}")

    def transform(self, data):
        """
        Apply transformations to the extracted data.
        :param data: Data to transform.
        """
        try:
            transformed_data = data.drop(["attributes"], axis=1)
            print("Data transformation completed.")
            return transformed_data
        except Exception as e:
            raise RuntimeError(f"Failed to transform data: {e}")

    def load(self, data):
        """
        Load data into the target database.
        :param data: Data to load.
        """
        try:
            if isinstance(self.target_connector.connection, pd.io.sql.SQLDatabase):
                data.to_sql("accounts", con=self.target_connector.connection, if_exists="replace", index=False)
            else:
                raise ValueError("Unsupported target for loading.")
            print("Data successfully loaded to the target database.")
        except Exception as e:
            raise RuntimeError(f"Failed to load data: {e}")
