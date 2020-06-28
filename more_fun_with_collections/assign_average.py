"""

Program: assign_average.py

Author: Chase Van Blair

Last date modified: 6/28/20


The purpose of this program is to create an artificial switch case in python

"""


def switch_average(user_dict, key):
    """
    this function emulates a switch function and either returns the item or none if not in dict
    :param user_dict: dict to be used for case
    :param key: key that determines how case runs
    :return: either value of the key or none
    """
    user_key = str(key).upper()
    if user_key in user_dict:
        if user_key == 'A':
            print("thats an a")
            return user_dict.get('A')
        elif user_key == 'B':
            print("thats a b")
            return user_dict.get('B')
        elif user_key == 'C':
            print("thats a c")
            return user_dict.get('C')
        elif user_key == 'D':
            print("thats a d")
            return user_dict.get('D')
        elif user_key == 'E':
            print("thats an e")
            return user_dict.get('E')
    else:
        print("thats nothing")
        return None
