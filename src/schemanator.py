from enum import auto, StrEnum
import json
import re

_INT_RE = re.compile(r"\d+")
_FLOAT_RE = re.compile(r"\d+\.\d+")
EmanatedSchema = dict[str, "SchemanatedType"]

class SchemanatedType(StrEnum):
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    JSON_OBJECT = "JSONObject"
    JSON_ARRAY = "JSONArray"
    # Any is only used for fields that take on different types throughout the
    # given dataset.
    ANY = auto()

    @classmethod
    def decide(cls, s):
        if _INT_RE.fullmatch(s):
            return cls.INTEGER
        elif _FLOAT_RE.fullmatch(s):
            return cls.FLOAT
        elif s[0] == "[" and s[-1] == "]":
            try:
                parse = json.loads(s)
                return cls.JSON_ARRAY
            except json.JSONDecodeError:
                return cls.STRING
        elif s[0] == "{" and s[-1] == "}":
            try:
                parse = json.loads(s)
                return cls.JSON_OBJECT
            except json.JSONDecodeError:
                return cls.STRING

        return cls.STRING

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
        inferred_schema: EmanatedSchema = {}
        for d in data:
            current_schema: EmanatedSchema = {}
            for k in d:
                val = d[k]
                current_schema[k] = SchemanatedType.decide(val)

            inferred_schema = self.__merge_schemas(
                inferred_schema, current_schema
            )

    def __merge_schemas(self, s1: EmanatedSchema, s2: EmanatedSchema):
        # Stub
        return s1
