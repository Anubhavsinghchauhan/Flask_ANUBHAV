import pytest
from square import sq

def test_check():
    assert sq(2) == 4
    assert sq(3) == 9
    assert sq(4) == 16
    assert sq(5) == 25  
    assert sq(6) == 36
    assert sq(7) == 49
    assert sq(8) == 64
    assert sq(9) == 81
    assert sq(10) == 100
    assert sq(11) == 121
    