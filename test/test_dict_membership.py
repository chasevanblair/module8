import unittest

from more_fun_with_collections.dict_membership import in_dict


class TestDict(unittest.TestCase):
    def test_in_dict_true(self):
        my_dict = {'A': 3, 'B': 44, 'C': 8}
        self.assertTrue(in_dict(my_dict, 'A'))

    def test_in_dict_false(self):
        my_dict = {'A': 3, 'B': 44, 'C': 8}
        self.assertFalse(in_dict(my_dict, 'D'))
