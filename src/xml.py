import xmltodict

from .data_transformer import DataTransformer
from .schemanator import EmanatedSchema, RawDataSet

from typing import Iterable

class XMLDataTransformer(DataTransformer):

    def parse_to_raw_data(self, dataset: Iterable[str]) -> RawDataSet:
        return [
            xmltodict.parse(item) for item in dataset
        ]

    def parse_to_schema(self, s: str) -> EmanatedSchema:
        return {}
