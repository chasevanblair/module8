import unittest

from more_fun_with_collections.dict_membership import in_dict


class TestDict(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertTrue(in_dict())

    def test_in_dict_false(self):
        self.assertFalse(in_dict())