import pytest


@pytest.mark.parametrize("num, output", [(1, 11),(2, 22),(3, 35),(4, 45)])
def test_multiply_11(num,output):
    assert 11*num == output