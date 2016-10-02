import unittest
import breakable


class TestNeeds(unittest.TestCase):
    def test_needs_missing(self):
        with self.assertRaises(Exception):
            breakable.needs("safkwlEUNFB")

    def test_needs_valid(self):
        breakable.needs("README.md")
