import unittest
import breakable


class TestFindFiles(unittest.TestCase):
    def test_find_files(self):
        items = list(breakable.find_files(r".*\.py", "tests/find_files"))
        self.assertEqual(len(items), 2)
        self.assertTrue("tests/find_files/1.py" in items)
        self.assertTrue("tests/find_files/2.py" in items)
