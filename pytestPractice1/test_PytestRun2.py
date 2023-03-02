import pytest


def test_TC4():
    name = "Monkey D Luffy "
    uppercasename = name.upper()
    assert name.upper() == uppercasename

def test_TC5():
    assert False

def test_TC6():
    assert 8+5 == 13

@pytest.mark.sampleMark
def test_TC7():
    name = "Naruto Uzumaki"
    uppercasename = name.upper()
    assert name.upper() == uppercasename
@pytest.mark.sampleMark
def test_AssertTrue():
    assert True
@pytest.mark.sampleMark
# here mark indicates the marker and sampleMark is the name of the given marker
def test_TC9():
    assert 3+15 == 88


