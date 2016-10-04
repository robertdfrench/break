import breakable
import unittest


class TestProvides(unittest.TestCase):
    def test_run_if_not_exists(self):
        @breakable.provides("nothing")
        def dummy(self):
            return 5
        self.assertEqual(dummy(self), 5)

    def test_dont_run_if_exists(self):
        @breakable.provides("README.md")
        def dummy(self):
            return 5
        self.assertEqual(dummy(self), None)
