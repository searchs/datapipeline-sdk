import pytest
from metrics import Metrics

def test_metrics():
    metrics = Metrics()
    metrics.increment_ingested()
    metrics.increment_transformed()
    metrics.increment_output()
    # Assert the counts if necessary
    assert metrics.ingested_messages._value.get() == 1
    assert metrics.transformed_messages._value.get() == 1
    assert metrics.output_messages._value.get() == 1

# Run the tests
# pytest test_metrics.py
