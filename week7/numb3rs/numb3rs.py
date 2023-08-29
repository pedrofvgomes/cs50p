import re
import sys

def main():
    a =(input('IPv4 Address:'))
    if validate(a):
        print('Valid')
    else:
        print('Invalid')

def validate(ip):
    # no formato X.X.X.X, X >= 0, X <= 255

    ip = ip.strip()

    try:
        first, second, third, fourth = ip.split('.')
    except ValueError:
        return False

    if first and second and third and fourth:
        try:
            return int(first) >= 0 and int(first) <= 255 and int(second) >= 0 and int(second) <= 255 and int(third) >= 0 and int(third) <= 255 and int(fourth) >= 0 and int(fourth) <= 255
        except ValueError:
            return False
    
    return False
if __name__ == '__main__':
    main()