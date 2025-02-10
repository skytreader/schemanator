import unittest

from ..schemanator import SchemanatedType

class SchemanatedTypeTests(unittest.TestCase):

    def test_decide(self):
        self.assertEqual(
            SchemanatedType.INTEGER,
            SchemanatedType.decide("1")
        )
