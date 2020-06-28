import unittest
"""

Program: test_assign_average.py

Author: Your Name

Last date modified: MM/DD/YYYY


The purpose of this program is to accept any input, 
convert to a integer type and output the integer. 

"""


from more_fun_with_collections.assign_average import switch_average


class TestAverage(unittest.TestCase):
    def test_a(self):
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = 'a'
        self.assertEqual(3, switch_average(user_dict, user_key.upper()))

    def test_b(self):
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = 'B'
        self.assertEqual(4, switch_average(user_dict, user_key.upper()))

    def test_c(self):
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = 'C'
        self.assertEqual(5, switch_average(user_dict, user_key.upper()))

    def test_d(self):
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = 'd'
        self.assertEqual(6, switch_average(user_dict, user_key.upper()))

    def test_e(self):
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = 'e'
        self.assertEqual(7, switch_average(user_dict, user_key.upper()))

    def test_none(self):
        user_dict = {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7}
        user_key = ''
        self.assertEqual(None, switch_average(user_dict, user_key.upper()))
