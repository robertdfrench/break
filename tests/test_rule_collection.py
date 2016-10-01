import unittest
import breakable


class TestRuleCollection(unittest.TestCase):
    def test_get(self):
        rc = breakable.RuleCollection()
        rc.internal_storage['poop'] = 5
        self.assertEqual(rc['poop'], 5)

    def test_first_is_default(self):
        rc = breakable.RuleCollection()
        rc['first'] = 1
        self.assertEqual(rc.default, 'first')

    def test_second_aint_default(self):
        rc = breakable.RuleCollection()
        rc['first'] = 1
        rc['second'] = 1
        self.assertNotEqual(rc.default, 'second')

    def test_to_string(self):
        rc = breakable.RuleCollection()
        rc['first'] = 1
        rc['second'] = 1
        self.assertEqual("%s" % rc, "Entrypoints:\n  first: 1\n  second: 1")
