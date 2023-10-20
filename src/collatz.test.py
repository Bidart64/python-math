import unittest
from collatz import collatz


class TestCollatz(unittest.TestCase):

    def test_collatz_with_1(self):
        self.assertEqual(collatz(1), 1)

    def test_collatz_with_2(self):
        self.assertEqual(collatz(2), 1)

    def test_collatz_with_3(self):
        self.assertEqual(collatz(3), 1)

    def test_collatz_with_4(self):
        self.assertEqual(collatz(4), 1)

    def test_collatz_with_5(self):
        self.assertEqual(collatz(5), 1)

    def test_collatz_with_6(self):
        self.assertEqual(collatz(6), 1)

    def test_collatz_with_7(self):
        self.assertEqual(collatz(7), 1)

    def test_collatz_with_8(self):
        self.assertEqual(collatz(8), 1)

    def test_collatz_with_9(self):
        self.assertEqual(collatz(9), 1)

    def test_collatz_with_10(self):
        self.assertEqual(collatz(10), 1)


if __name__ == '__main__':
    unittest.main()
