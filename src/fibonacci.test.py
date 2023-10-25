import unittest
from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_with_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_with_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_with_3(self):
        self.assertEqual(fibonacci(3), 2)

    def test_fibonacci_with_4(self):
        self.assertEqual(fibonacci(4), 3)

    def test_fibonacci_with_5(self):
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_with_6(self):
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_with_7(self):
        self.assertEqual(fibonacci(7), 13)

    def test_fibonacci_with_8(self):
        self.assertEqual(fibonacci(8), 21)

    def test_fibonacci_with_9(self):
        self.assertEqual(fibonacci(9), 34)


if __name__ == '__main__':
    unittest.main()
