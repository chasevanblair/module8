"""

Program: dict_update.py

Author: Chase Van Blair

Last date modified: 6/28/20


The purpose of this program is to take user input for test scores and insert scores
in a dict, then pass that dict to average_scores() to calculate the average

"""


def get_test_scores():
    """
    takes input from user and stores it in scores_dict
    :return: dict of scores from user
    """
    scores_dict = dict()
    num = 0
    x = 0
    while x != -1:
        try:
            x = int(input("Enter student score or -1 to stop: "))
        except ValueError:
            print("numbers only")
        num += 1
        if x != -1:
            scores_dict.update({str(num): x})

    return scores_dict


def average_scores(user_dict):
    """
    return the average of the scores from get_test_scores
    :param user_dict: the dict from get_test_scores
    :return: average of user_dict
    """
    total = 0
    for x in range(1, len(user_dict) + 1):
        total += user_dict.get(str(x))

    return total / len(user_dict)


if __name__ == '__main__':
    my_dict = get_test_scores()
    print("average of dict is %s" % average_scores(my_dict))
