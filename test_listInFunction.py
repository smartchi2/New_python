from this import s
from unittest import TestCase
from listInFunction import number, nums, AverageNumbers


class Test(TestCase):
    def test_number(self):
        self.assertEquals(number(), 51, 100)


class Test(TestCase):
    def test_getNumber_length(self, nums=6):
        self.assertEqual(6, nums, 5)


class Test(TestCase):
    def test_getEvenNumber(self, number: object = 56):
        self.assertEqual(number, 56, 7)


class Test(TestCase):
    def test_multiply(self):
        self.assertEqual(input(), [12, 24, 56, 30, 20, 4], [12, 24, 56, 30, 2, 5])


class Test(TestCase):
    def test_AverageNumbers(self):
        self.assertEqual(AverageNumbers([12, 45, 70]), 42.33)
