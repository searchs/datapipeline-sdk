from abc import ABC, abstractmethod

class TransformationPlugin(ABC):
    @abstractmethod
    def transform(self, data):
        pass
