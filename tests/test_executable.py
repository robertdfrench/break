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

    def test_collect(self):
        mock_echo = breakable.Executable("tests/mock_echo")
        output = ''.join(mock_echo.collect("'hello\nmy-son'"))
        self.assertEqual("hello my-son", output.rstrip())

if __name__ == '__main__':
    unittest.main()
