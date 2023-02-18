import unittest
from main_f import A


class TestA(unittest.TestCase):

    def setUp(self) -> None:
        self.a = A()

    def test_a(self):
        self.assertEqual(self.a.func(5), 25)

    def test_b(self):
        self.assertEqual(self.a.f(5, 5), 25)


if __name__ == '__main__':
    unittest.main()