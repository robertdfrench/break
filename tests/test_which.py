#!/usr/bin/env python
import unittest
import breakable


class TestWhich(unittest.TestCase):
    def test_which_specific_path(self):
        mock_exe = breakable.which('tests/mock_executable')
        output = mock_exe()
        self.assertEqual("Welcome to the machine", ("%s" % output).rstrip())

    def test_which_search(self):
        python = breakable.which('python')
        output = python(" -c 'print(\"Welcome to the machine\")'")
        self.assertEqual("Welcome to the machine", ("%s" % output).rstrip())

    def test_bad_search_is_none(self):
        bad_program = breakable.which('crapola')
        self.assertIsNone(bad_program)


if __name__ == '__main__':
    unittest.main()
