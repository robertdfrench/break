#!/usr/bin/env python
import unittest
import breakable


class TestLog(unittest.TestCase):
    def test_log_print(self):
        breakable.log._print('plain')

    def test_log_print_prefix(self):
        breakable.log._print('plain', prefix='==>')

    def test_log_print_color(self):
        breakable.log._print('plain', color=breakable.log.red)

    def test_exercise_info(self):
        breakable.log.info('Hello, World!')

if __name__ == '__main__':
    unittest.main()
