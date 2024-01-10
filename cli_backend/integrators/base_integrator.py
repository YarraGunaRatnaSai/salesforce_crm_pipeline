class BaseIntegrator:
    """
    Base class for data integrators.
    """
    def __init__(self, source_connector, target_connector):
        """
        Initialize the integrator with source and target connectors.
        :param source_connector: Connector for the data source.
        :param target_connector: Connector for the data target.
        """
        self.source_connector = source_connector
        self.target_connector = target_connector

    def extract(self):
        """
        Extract data from the source.
        """
        raise NotImplementedError("Extract method must be implemented in subclasses.")

    def transform(self, data):
        """
        Transform the data.
        :param data: Data to transform.
        """
        raise NotImplementedError("Transform method must be implemented in subclasses.")

    def load(self, data):
        """
        Load data into the target.
        :param data: Data to load.
        """
        raise NotImplementedError("Load method must be implemented in subclasses.")

    def execute(self):
        """
        Execute the ETL process: Extract, Transform, and Load.
        """
        data = self.extract()
        transformed_data = self.transform(data)
        self.load(transformed_data)
