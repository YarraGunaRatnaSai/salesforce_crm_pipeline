import hashlib
import os

class Tracker:
    """
    Tracks processed records using hash values.
    """
    def __init__(self, log_file="cli_backend/logs/metadata-log.txt"):
        """
        Initialize the tracker with a log file.
        :param log_file: Path to the metadata log file.
        """
        self.log_file = log_file
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as file:
                file.write("record_hash\n")

    def generate_hash(self, record):
        """
        Generate a hash for a record.
        :param record: Record to hash.
        """
        record_string = str(record)
        return hashlib.sha256(record_string.encode()).hexdigest()

    def is_processed(self, record_hash):
        """
        Check if a record has already been processed.
        :param record_hash: Hash of the record.
        """
        with open(self.log_file, "r") as file:
            processed_hashes = file.read().splitlines()
            return record_hash in processed_hashes

    def log_processed(self, record_hash):
        """
        Log a processed record's hash.
        :param record_hash: Hash of the record.
        """
        with open(self.log_file, "a") as file:
            file.write(record_hash + "\n")
