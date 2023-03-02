import pytest


def test_printName():
    name = "manikanth"
    uppercasename = name.upper()
    assert name.upper() == uppercasename
@pytest.mark.sampleMark
def test_TC2():
    assert True

def test_TC3():
    assert 3+5 == 8



