from fuel import gauge, convert
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("2/3") == 67
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    with pytest.raises(ValueError):
        assert convert("3/2")
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")

def test_gauge(): 
    assert gauge(1) == "E" 
    assert gauge(0) == "E" 
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(45) == "45%"

if __name__ == '__main__':
    main()