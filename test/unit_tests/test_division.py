from lib import division
import pytest

def test_divide_2_numbers():
    assert 2 == division.divide_2_numbers(6, 3),"6 and 3 division failed"
