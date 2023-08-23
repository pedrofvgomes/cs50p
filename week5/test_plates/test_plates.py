from plates import is_valid

def main():
    test_is_valid()

def test_is_valid():
    assert is_valid('1dkad') == False
    assert is_valid('aa0') == False
    assert is_valid('aa1') == True
    assert is_valid('AA1A') == False
    assert is_valid('aidhwaidah') == False
    assert is_valid('PI3.14') == False
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False
    assert is_valid('1234125') == False
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False
    assert is_valid('aaa222') == True
    assert is_valid('aaa22a') == False
    assert is_valid('PI 14') == False    

if __name__ == '__main__':
    main()