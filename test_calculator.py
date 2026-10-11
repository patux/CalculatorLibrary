"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)
        assert 2 == calculator.add(-3, 5)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
        assert -8 == calculator.subtract(-3, 5)

    def test_multiplication(self):
        assert 6 == calculator.multiply(2, 3)
        assert -15 == calculator.multiply(-3, 5)
