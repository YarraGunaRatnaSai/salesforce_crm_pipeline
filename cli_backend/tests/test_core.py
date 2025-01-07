import pytest
from cli_backend.core.data_mapper import DataMapper

def test_data_mapper_apply_mapping():
    """
    Test the application of mapping rules.
    """
    mapper = DataMapper()
    data = {"old_name": "Alice", "old_age": 25}
    mapping = {"old_name": "name", "old_age": "age"}
    mapped_data = mapper.apply_mapping(data, mapping)
    assert mapped_data == {"name": "Alice", "age": 25}
