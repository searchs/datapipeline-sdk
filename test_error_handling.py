import pytest
from error_handling import IngestionError, TransformationError, OutputError

def test_ingestion_error():
    with pytest.raises(IngestionError):
        raise IngestionError("Test Ingestion Error")

def test_transformation_error():
    with pytest.raises(TransformationError):
        raise TransformationError("Test Transformation Error")

def test_output_error():
    with pytest.raises(OutputError):
        raise OutputError("Test Output Error")

# Run the tests
# pytest test_error_handling.py
