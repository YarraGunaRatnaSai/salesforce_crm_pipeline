from simple_salesforce import Salesforce

class SalesforceConnector:
    """
    Connector for Salesforce.
    """
    def __init__(self, username: str, password: str, token: str):
        """
        Initialize the Salesforce connector.
        :param username: Salesforce username.
        :param password: Salesforce password.
        :param token: Salesforce security token.
        """
        self.username = username
        self.password = password
        self.token = token
        self.connection = None

    def connect(self):
        """
        Establish connection to Salesforce.
        """
        try:
            self.connection = Salesforce(username=self.username, password=self.password, security_token=self.token)
            print("Salesforce connection established.")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Salesforce: {e}")
