from enum import auto, StrEnum
import re

class SchemanatedType(StrEnum):
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    JSON_OBJECT = "JSONObject"
    JSON_ARRAY = "JSONArray"
    ANY = auto()

    @classmethod
    def decide(cls, s):
        return cls.ANY

class Schemanator(object):

    def __init__(
        self,
        ignore_inconsistent=False,
        quoted_strings=False,
        enumerate_union=False
    ):
        self.ignore_inconsistent = ignore_inconsistent
        self.quoted_strings = quoted_strings
        self.enumerate_union = enumerate_union

    def emanate(self, data:list[dict[str, str]]):
        for d in data:
            for k,v in d:
                pass                
