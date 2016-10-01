import unittest
import breakable


class TestEntrypoint(unittest.TestCase):
    def test_define_entrypoint(self):
        @breakable.entrypoint
        def dummy_entrypoint():
            pass
