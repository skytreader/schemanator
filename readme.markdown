# schememanator

Generate schemas out of collections of data. Can output data schemas in its own
JSON format, [JSON Schema](https://json-schema.org/), or
[XSD](https://www.w3.org/TR/xmlschema-0/). Extensible for other schema
specifications.

Input can be XML or JSON. Other input formats can be easily accomodated.

## Data types

The fields in your data set will be tagged with the following data types:

- `integer` for integers (in the mathematical sense of the word)
- `float` for floating point
- `string` for strings
- `JSONObject` for obviously-JSON objects
- `JSONArray` for obviously-JSON arrays
- `any` for fields that can take on multiple types

## Flags

`-i --ignore-inconsistent` Allows fields to have inconsistent typing and be
tagged as `any`. Without this flag, schememanator will throw and exception and
quit for inconsistent data sets.

`-q --quoted-strings` Every field in quotes (double or single) will be treated
as strings. Otherwise, schememanator will attempt to predict the type of data
between the quotes.

`-e --enumerate-union` For fields that can take on multiple types, enumerate the
possible types found in the data set.
