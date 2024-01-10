import psycopg2
from pymongo import MongoClient

class DatabaseConnector:
    """
    Connector for SQL and NoSQL databases.
    """
    def __init__(self, db_type: str, config: dict):
        """
        Initialize the database connector.
        :param db_type: Type of database ('postgres' or 'mongo').
        :param config: Database configuration.
        """
        self.db_type = db_type
        self.config = config
        self.connection = None

    def connect(self):
        """
        Establish a connection to the database.
        """
        try:
            if self.db_type == "postgres":
                self.connection = psycopg2.connect(
                    dbname=self.config["dbname"],
                    user=self.config["user"],
                    password=self.config["password"],
                    host=self.config["host"],
                    port=self.config["port"],
                )
            elif self.db_type == "mongo":
                self.connection = MongoClient(self.config["uri"])
            else:
                raise ValueError(f"Unsupported database type: {self.db_type}")
            print(f"Connected to {self.db_type} database.")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to database: {e}")
