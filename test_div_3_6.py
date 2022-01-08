# import pytest
#
#
# @pytest.fixture
def input_value1():
    input = 39
    return input

def test_divisible_by_3(input_value1):
    assert input_value1 % 3 == 0


def test_divisible_by_6(input_value1):
    assert input_value1 % 6 == 0

