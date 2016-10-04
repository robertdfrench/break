import unittest
import breakable


class TestNeeds(unittest.TestCase):
    def test_needs_missing(self):
        with self.assertRaises(Exception):
            breakable.needs("safkwlEUNFB")

    def test_needs_valid(self):
        breakable.needs("README.md")

    def test_only_if_modified_not_modified(self):
        @breakable.only_if_modified("README.md")
        def dummy(self):
            return 5
        self.assertEqual(dummy(self), None)
        breakable.rm(".breakstamp.dummy")

    def test_only_if_modified(self):
        breakable.rm(".breakstamp.dummy")

        @breakable.only_if_modified("README.md")
        def dummy(self):
            return 5
        self.assertEqual(dummy(self), 5)
