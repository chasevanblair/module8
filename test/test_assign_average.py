import unittest
"""

Program: test_assign_average.py

Author: Chase Van Blair

Last date modified: 6/28/20


The purpose of this program is to test the artificial switch
case made in assign_average.py

"""


from more_fun_with_collections.assign_average import switch_average


class TestAverage(unittest.TestCase):
    def test_a(self):
        """
        test switch_average() when passed A
        :return:
        """
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = 'a'
        self.assertEqual(3, switch_average(user_dict, user_key.upper()))

    def test_b(self):
        """
        test switch_average() when passed b
        :return:
        """
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = 'B'
        self.assertEqual(4, switch_average(user_dict, user_key.upper()))

    def test_c(self):
        """
        test switch_average() when passed c
        :return:
        """
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = 'C'
        self.assertEqual(5, switch_average(user_dict, user_key.upper()))

    def test_d(self):
        """
        test switch_average() when passed d
        :return:
        """
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = 'd'
        self.assertEqual(6, switch_average(user_dict, user_key.upper()))

    def test_e(self):
        """
        test switch_average() when passed e
        :return:
        """
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = 'e'
        self.assertEqual(7, switch_average(user_dict, user_key.upper()))

    def test_none(self):
        """
        test switch_average() when passed a key thats not in the dict
        :return:
        """
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = ''
        self.assertEqual(None, switch_average(user_dict, user_key.upper()))
