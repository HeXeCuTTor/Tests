import unittest
from unittest import TestCase
from old_hometasks import task_1, task_2, task_3


class HomeworkTask_1(TestCase):
    def test_1(self):
        res = task_1()
        self.assertNotIsInstance(res, dict)
        self.assertListEqual(res,[{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}])
  
class HomeworkTask_2(TestCase):  
    def test_2(self):
        res = task_2()
        self.assertIsInstance(res, set)
        self.assertSetEqual(res,{98, 35, 213, 54, 119, 15})

class HomeworkTask_3(TestCase):
    def test_3(self):
        res = task_3()
        self.assertIsInstance(res, str)
        self.assertEqual(res,"yandex")

if __name__ == '__main__':
    unittest.main()