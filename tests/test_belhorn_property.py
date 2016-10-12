import unittest
import breakable


class Dummy(object):

    def __init__(self):
        self.number_of_times_property_was_calculated = 0

    @breakable.belhorn_property
    def cool_property(self):
        self.number_of_times_property_was_calculated += 1
        return 5


class TestBelhornProperty(unittest.TestCase):
    def test_dummy_property_starts_with_clean_slate(self):
        x = Dummy()
        self.assertEqual(x.number_of_times_property_was_calculated, 0)

    def test_belhorn_property_returns_expected_value(self):
        x = Dummy()
        self.assertEqual(x.cool_property, 5)

    def test_belhorn_property_only_computes_once(self):
        x = Dummy()
        x.cool_property
        x.cool_property
        self.assertEqual(x.number_of_times_property_was_calculated, 1)
