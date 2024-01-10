import pytest
from cli_backend.metadata.tracker import Tracker

def test_tracker_logging():
    """
    Test logging of record hashes in Tracker.
    """
    tracker = Tracker(log_file="test_metadata_log.txt")
    record = {"name": "Alice", "age": 25}
    record_hash = tracker.generate_hash(record)

    assert not tracker.is_processed(record_hash)
    tracker.log_processed(record_hash)
    assert tracker.is_processed(record_hash)
