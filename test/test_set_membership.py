import unittest

from more_fun_with_collections.set_membership import in_set


class TestMembership(unittest.TestCase):
    def test_in_set_true(self):
        my_set = {1, 2, 3, 4, 5}
        self.assertTrue(in_set(my_set, 3))

    def test_in_set_false(self):
        my_set = {1, 2, 3, 4, 5}
        self.assertFalse(in_set(my_set, 12))
