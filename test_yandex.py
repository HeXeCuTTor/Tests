import unittest
from unittest import TestCase
from yandex import Yandex

class YandexTest(TestCase):    

    def test_ya(self):
        res = Yandex()
        self.assertIsInstance(res, int)
        self.assertEqual(res, 201)  

class YandexTest_failure(TestCase):

    @unittest.expectedFailure
    def test_failure(self):
        res = Yandex()
        self.assertEqual(res,201)
        self.assertEqual(res,200)

if __name__ == '__main__':
    unittest.main()