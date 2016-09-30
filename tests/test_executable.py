#!/usr/bin/env python
import unittest
import breakable


class TestExecutable(unittest.TestCase):
    def test_call(self):
        mock_exe = breakable.Executable("tests/mock_executable")
        for line in mock_exe():
            self.assertEqual(line.rstrip(), "Welcome to the machine")

    def test_buffer_call(self):
        mock_exe = breakable.Executable("tests/mock_executable")
        output = mock_exe()
        self.assertEqual("Welcome to the machine", ("%s" % output).rstrip())

    def test_options(self):
        mock_echo = breakable.Executable("tests/mock_echo")
        output = mock_echo("we-know-where-youve-been")
        self.assertEqual("we-know-where-youve-been", ("%s" % output).rstrip())

if __name__ == '__main__':
    unittest.main()
