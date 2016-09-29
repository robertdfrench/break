#!/usr/bin/env python
import unittest
import dummy


class TestDummt(unittest.TestCase):
    def test_hello(self):
        dummy.hello()

if __name__ == '__main__':
    unittest.main()
