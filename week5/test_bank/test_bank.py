from bank import value

def main():
    test_value()

def test_value():
    assert value('hello pedro') == 0
    assert value('hi pedro') == 20
    assert value('wassup') == 100 

if __name__ == '__main__':
    main()