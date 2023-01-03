import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(5, 1) == 6

    def test_multiply_success(self):
        assert self.calc.multiply(3, 5) == 15

    def test_division_success(self):
        assert self.calc.division(21, 3) == 7

    def test_subtraction_success(self):
        assert self.calc.subtraction(12, 6) == 6


    def teardown(self):
        print('Выполнение метода Teardown')