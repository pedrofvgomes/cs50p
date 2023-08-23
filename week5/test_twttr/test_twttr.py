from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten('abebibobub') == 'bbbbb'
    assert shorten('aeiou') == ''
    assert shorten('a daiwj e nedjfe') == ' dwj  ndjf'
    assert shorten('DUAHWDHAWDHAW') == 'DHWDHWDHW'

if __name__ == '__main__':
    main()