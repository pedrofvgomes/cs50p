from seasons import convert

def main():
    test_convert()

def test_convert():
    assert convert('2022-08-29') == 'Five hundred twenty-five thousand, six hundred minutes'
    assert convert('10-08-29') == None

if __name__ == '__main__':
    main()