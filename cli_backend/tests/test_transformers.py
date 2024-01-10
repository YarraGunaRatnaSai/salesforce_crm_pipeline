import pytest
from cli_backend.core.transformer import DataTransformer

def test_transformer_apply_transformation():
    """
    Test applying transformation rules to data.
    """
    transformer = DataTransformer()
    data = {"name": "Alice", "age": 25}
    rules = {"age": lambda x: x + 5}
    transformed_data = transformer.apply_transformation(data, rules)
    assert transformed_data["age"] == 30
