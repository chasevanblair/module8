import unittest
from datetime import datetime, timedelta

from more_fun_with_collections.date_time import half_birthday


class TestDate(unittest.TestCase):
    def test_half_birthday(self):
        bday = datetime.datetime(2020, 5, 16)
        half = bday + timedelta(days=60)
        self.assertEqual(half, half_birthday(bday))
