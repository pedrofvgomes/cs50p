from response import validate

def main():
    test_validate()

def test_validate():
    assert validate('malan@harvard.edu') == True
    assert validate('pedro@gmail.com') == True
    assert validate('malan@@harvard.edu') == False
    assert validate('malan@harvard..edu') == False
    

if __name__ == '__main__':
    main()