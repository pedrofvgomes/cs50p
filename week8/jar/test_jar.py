from jar import Jar
import pytest

def main():
    test_jar()
    test_deposit()
    test_withdraw()
    test_str()


def test_jar():
    # valid
    j = Jar(10)
    assert j.size == 0
    assert j.capacity == 10

    # invalid
    with pytest.raises(ValueError):
        assert Jar(-10)
    with pytest.raises(ValueError):
        assert j.deposit(11)
    with pytest.raises(ValueError):
        assert j.withdraw(100)

def test_deposit():
    j = Jar(10)
    assert j.size == 0
    j.deposit(2)
    assert j.size == 2

def test_withdraw():
    j = Jar(10)
    j.deposit(2)
    assert j.size == 2
    j.withdraw(1)
    assert j.size == 1

def test_str():
    j = Jar(10)
    assert str(j) == ''
    j.deposit(1)
    assert str(j) == '🍪'
    j.deposit(1)
    assert str(j) == '🍪🍪'



if __name__ == '__main__':
    main()