import unittest
import breakable


class TestBreakPath(unittest.TestCase):
    def test_newer_than(self):
        touch = breakable.which("touch")
        touch("newfile")
        self.assertTrue(breakable.path("newfile").newer_than("README.md"))
        breakable.rm("newfile")

    def test_raises_if_left_doesnt_exist(self):
        with self.assertRaises(Exception):
            breakable.path("nothing").newer_than("README.md")

    def test_raises_if_right_doesnt_exist(self):
        with self.assertRaises(Exception):
            breakable.path("README.md").newer_than("nothing")

    def test_dirtier_than(self):
        self.assertTrue(breakable.path("README.pdf").dirtier_than("README.md"))

    def test_raises_if_dependency_doesnt_exist(self):
        with self.assertRaises(Exception):
            breakable.path("nothing.pdf").dirtier_than("nothing.md")
