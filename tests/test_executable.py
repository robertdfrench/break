#!/usr/bin/env python
import unittest
import breakable


class TestExecutable(unittest.TestCase):
    def test_call(self):
        mock_exe = breakable.Executable("tests/mock_executable")
        mock_exe()

    def test_options(self):
        mock_echo = breakable.Executable("tests/mock_echo")
        mock_echo("we-know-where-youve-been")


if __name__ == '__main__':
    unittest.main()
