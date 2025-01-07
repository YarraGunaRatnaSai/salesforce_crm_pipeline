import logging

class ErrorHandler:
    """
    Handles errors and logs them.
    """
    def __init__(self, logger_name: str = "error_handler"):
        """
        Initialize the error handler with a logger.
        :param logger_name: Name of the logger.
        """
        self.logger = logging.getLogger(logger_name)

    def log_error(self, error: Exception):
        """
        Log an error message.
        :param error: Exception object.
        """
        self.logger.error(f"Error occurred: {error}")

    def raise_error(self, error: Exception):
        """
        Log and raise an error.
        :param error: Exception object.
        """
        self.log_error(error)
        raise error
