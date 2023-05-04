import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_succes(self):
        assert self.calc.adding(1, 1)==2

    def test_multiply_succes(self):
        assert self.calc.multiply(2, 3) == 6


    def test_division_succes(self):
         assert self.calc.division(10,5) ==2

    def test_subtraction_succes(self):
        assert self.calc.subtraction(10, 3)==7



    def teardown(self):
        print("Выполнение метода Teardown")