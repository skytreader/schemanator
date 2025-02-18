from enum import auto, StrEnum
from .errors import InconsistentDataError
from typing import Iterable, Optional, Sequence

import copy
import json
import re

_INT_RE = re.compile(r"\d+")
_FLOAT_RE = re.compile(r"\d+\.\d+")
EmanatedSchema = dict[str, set["SchemanatedType"]]
RawDataSet = Iterable[dict[str, str]]

class SchemanatedType(StrEnum):
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    JSON_OBJECT = "JSONObject"
    JSON_ARRAY = "JSONArray"
    # Any is only used for fields that take on different types throughout the
    # given dataset.
    ANY = auto()
    OPTIONAL = auto()

    @classmethod
    def decide(cls, s: str) -> "SchemanatedType":
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
        self.type_collisions: dict[str, set[SchemanatedType]] = {}

    def emanate(self, data: RawDataSet) -> EmanatedSchema:
        inferred_schema: EmanatedSchema = {}
        for d in data:
            current_schema: EmanatedSchema = {}
            for k in d:
                val = str(d[k])
                current_schema[k] = set((SchemanatedType.decide(val),))

            inferred_schema = self.__merge_schemas(
                inferred_schema, current_schema
            )

        return inferred_schema

    def __unpack_schema_type(self, schema_type: set[SchemanatedType]) -> SchemanatedType:
        if len(schema_type) == 1:
            return tuple(schema_type)[0]
        return SchemanatedType.ANY

    def __merge_schemas(self, s1: EmanatedSchema, s2: EmanatedSchema) -> EmanatedSchema:
        s1_keys = set(s1.keys())
        s2_keys = set(s2.keys())
        uniq_s2_keys = s2_keys.difference(s1_keys)
        working_schema = copy.deepcopy(s1)
        any_typed_keys = []

        for s1k in s1_keys:
            s2_type = s2.get(s1k)
            if working_schema[s1k] != s2_type:
                if self.ignore_inconsistent:
                    if s2_type:
                        if not self.enumerate_union:
                            working_schema[s1k] = set((SchemanatedType.ANY,))
                        else:
                            any_typed_keys.append(s1k)

                        s1k_known_types = self.type_collisions.get(s1k, set())
                        s1k_known_types.add(self.__unpack_schema_type(s1[s1k]))
                        s1k_known_types.add(self.__unpack_schema_type(s2_type))
                    else:
                        working_schema[s1k] = set((SchemanatedType.OPTIONAL,))
                else:
                    raise InconsistentDataError(s1k, s1[s1k], s2.get(s1k))

        for uk in uniq_s2_keys:
            working_schema[uk] = s2[uk]

        # Invariant: any_typed_keys can only be non-empty if enumerate_union is True
        for schema_key in any_typed_keys:
            working_schema[schema_key] = self.type_collisions[schema_key]

        return working_schema
