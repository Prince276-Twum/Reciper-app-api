""""
Sample tests
"""


from django.test import SimpleTestCase
from app import cal


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):

        res = cal.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        res = cal.subtract(7, 6)
        self.assertEqual(res, 1)
