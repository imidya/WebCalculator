import pytest
from Calculator import Calculator
from collections import deque


@pytest.fixture(scope='module')
def c():
    return Calculator()


def test_process_add(c):
    result = c.process_add(deque([1, '+', 3]))
    assert result.pop() == 4


def test_process_minus(c):
    result = c.process_minus(deque([3, '-', 1]))
    assert result.pop() == 2


def test_process_times(c):
    result = c.process_times(deque([2, '*', 3]))
    assert result.pop() == 6


def test_process_divided(c):
    result = c.process_add(deque([9, '/', 3]))
    assert result.pop() == 3


def test_add(c):
    result = c.cal('1+2+3+4+15')
    assert result == 25


def test_minus(c):
    result = c.cal('100-5-6-7-8-9')
    assert result == 65


def test_times(c):
    result = c.cal('1*2*3*4')
    assert result == 24


def test_divided(c):
    result = c.cal('100/2/5/2')
    assert result == 5


def test_arithmetic(c):
    result = c.cal('100/2/5*2')
    assert result == 20
