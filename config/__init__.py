import yaml
import os

# Function to load YAML configuration files
def load_config(env="development"):
    config_file = f"{env}.yaml"
    config_path = os.path.join(os.path.dirname(__file__), config_file)
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    return config
