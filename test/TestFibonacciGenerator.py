from unittest import TestCase

from FibonacciGenerator import FibonacciGenerator


class TestFibonacciGenerator(TestCase):
    def setUp(self) -> None:
        self.fibonacci_generator = FibonacciGenerator()

    def test_generate_0_is_nothing(self):
        self.assertEqual([], list(self.fibonacci_generator.generate(0)))

    def test_1_is_0(self):
        self.assertEqual([0], list(self.fibonacci_generator.generate(1)))

    def test_2_is_01(self):
        self.assertEqual([0, 1], list(self.fibonacci_generator.generate(2)))

    def test_first_six_numbers(self):
        self.assertEqual([0, 1, 1, 2, 3, 5], list(self.fibonacci_generator.generate(6)))

    def test_first_nine_numbers(self):
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21], list(self.fibonacci_generator.generate(9)))

    def test_first_4_numbers_and_then_5_more(self):
        self.assertEqual([0, 1, 1, 2], list(self.fibonacci_generator.generate(4)))
        self.assertEqual([3, 5, 8, 13, 21], list(self.fibonacci_generator.generate(5)))


