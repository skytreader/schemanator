# schemanator

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
- `optional` for fields that may not always be present for each item. Optional
  fields will only be marked with either `--ignore-inconsistent` or
  `--enumerate-union`.

## Flags

`-i --ignore-inconsistent` Allows fields to have inconsistent typing and be
tagged as `any`. Without this flag, schemanator will throw an exception and quit
for inconsistent data sets.

> **TODO**
> 
> `-q --quoted-strings` Every field in quotes (double or single) will be treated
> as strings. Otherwise, schemanator will attempt to predict the type of data
> between the quotes.

`-e --enumerate-union` For fields that can take on multiple types, enumerate the
possible types found in the data set. Otherwise, they will only be marked as
`any`. This is basically a "stronger" signal than the `--ignore-inconsistent`
flag. The enumeration for optional types will only include the non-null types.
