"""

Program: test_dict_membership.py

Author: Chase Van Blair

Last date modified: 6/27/20


The purpose of this program is to get familiar with dictionaries
by testing the functions in dict_membership

"""
import unittest

from more_fun_with_collections.dict_membership import in_dict


class TestDict(unittest.TestCase):
    def test_in_dict_true(self):
        """
        test a true return from in_dict()
        :return:
        """
        my_dict = {'A': 3, 'B': 44, 'C': 8}
        self.assertTrue(in_dict(my_dict, 'A'))

    def test_in_dict_false(self):
        """
        test a false return from in_dict()
        :return:
        """
        my_dict = {'A': 3, 'B': 44, 'C': 8}
        self.assertFalse(in_dict(my_dict, 'D'))
