import yaml

class ConfigManager:
    """
    Manages configuration settings.
    """
    def __init__(self, config_file: str):
        """
        Initialize ConfigManager with a YAML configuration file.
        :param config_file: Path to the configuration file.
        """
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self):
        """
        Load the configuration from the YAML file.
        """
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get(self, key: str, default=None):
        """
        Retrieve a configuration value.
        :param key: Configuration key to retrieve.
        :param default: Default value if the key does not exist.
        """
        return self.config.get(key, default)
