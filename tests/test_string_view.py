#!/usr/bin/env python
import unittest
import breakable


class TestStringView(unittest.TestCase):
    def test_string_form(self):
        with open('tests/dummy_file.txt', 'r') as f:
            sv = breakable.StringView(f)
            self.assertEqual("Welcome to the machine", ("%s" % sv).rstrip())

    def test_iterator(self):
        with open('tests/dummy_file.txt', 'r') as f:
            sv = breakable.StringView(f)
            for line in sv:
                self.assertEqual("Welcome to the machine", line.rstrip())

if __name__ == '__main__':
    unittest.main()
