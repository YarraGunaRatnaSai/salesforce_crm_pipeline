class BaseConnector:
    """
    Abstract base class for all connectors.
    """
    def connect(self):
        """
        Establish a connection to the data source.
        """
        raise NotImplementedError("Subclasses must implement the 'connect' method.")
