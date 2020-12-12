from lib import addition
import pytest

def test_add_2_numbers():
    assert 5 == addition.add_2_numbers(2, 3),"2 and 3 addition failed"
