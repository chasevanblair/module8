import unittest

from more_fun_with_collections.set_membership import in_set


class TestMembership(unittest.TestCase):
    def test_in_set_true(self):
        self.assertTrue(in_set())

    def test_in_set_false(self):
        self.assertFalse(in_set())

