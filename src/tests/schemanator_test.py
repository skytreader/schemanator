import unittest

from ..schemanator import SchemanatedType

class SchemanatedTypeTests(unittest.TestCase):

    def test_decide(self):
        self.assertEqual(SchemanatedType.INTEGER, SchemanatedType.decide("1"))
        # Will not be read as float, like in Java notation
        self.assertEqual(SchemanatedType.STRING, SchemanatedType.decide("1f"))
        self.assertEqual(SchemanatedType.FLOAT, SchemanatedType.decide("1.0"))
        self.assertEqual(SchemanatedType.STRING, SchemanatedType.decide("2.0f"))

        # Only "" and not '' are valid strings in JSON
        self.assertEqual(
            SchemanatedType.STRING,
            SchemanatedType.decide("{'data': 'hello'}")
        )
        self.assertEqual(
            SchemanatedType.JSON_OBJECT,
            SchemanatedType.decide('{"data": "hello"}')
        )
        self.assertEqual(
            SchemanatedType.STRING,
            SchemanatedType.decide("[1a, 2,3,'4']")
        )
        self.assertEqual(
            SchemanatedType.JSON_ARRAY,
            SchemanatedType.decide("[1, 2, 3]")
        )
