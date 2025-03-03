from abc import ABC, abstractmethod
from .schemanator import EmanatedSchema, RawDataSet
from typing import Iterable

class DataTransformer(ABC):
    """
    A DataTransformer deals with data formats (such as XML and JSON) and
    transforms them into a format that Schemanator can understand. Each
    implementation of DataTransformer deals with only on data format.
    """

    @abstractmethod
    def parse_to_raw_data(self, dataset: Iterable[str]) -> RawDataSet:
        """
        Converts an iterable of data encoded in the original format and creates
        a RawDataSet out of it. Implementations are free to adapt their own
        conventions but data integrity must be preserved.
        """
        pass

    @abstractmethod
    def parse_to_schema(self, s: str) -> EmanatedSchema:
        """
        Converts a schema specification for the original format (such as XSD or
        JSON Schema) into an EmanatedSchema.
        """
        pass
