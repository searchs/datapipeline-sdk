class DataPipelineError(Exception):
    """Base class for other exceptions"""
    pass

class IngestionError(DataPipelineError):
    """Raised when an error occurs in the ingestion process"""
    pass

class TransformationError(DataPipelineError):
    """Raised when an error occurs in the transformation process"""
    pass

class OutputError(DataPipelineError):
    """Raised when an error occurs in the output process"""
    pass
