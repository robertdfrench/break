#!/usr/bin/env python
import unittest
import breakable


class TestLog(unittest.TestCase):
    def test_exercise_info(self):
        breakable.log.info('Hello, World!')

if __name__ == '__main__':
    unittest.main()
