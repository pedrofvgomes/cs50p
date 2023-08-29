import validators

def main():
    response = validate(input("What's your email address? "))
    if response:
        print('Valid')
    else:
        print('Invalid')



def validate(s):
    if s.count('@') != 1:
        return False

    local, domain = s.split('@')

    if not local or not domain:
        return False

    valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-'

    for char in local:
        if char not in valid:
            return False
    
    for char in domain:
        if char not in valid:
            return False

    if '..' in local or '..' in domain:
        return False
    
    if '.' not in domain:
        return False
    
    if domain[0] == '.' or domain[-1] == '.':
        return False
    
    if len(domain.split('.')[-1]) > 61:
        return False
    
    return True


if __name__ == '__main__':
    main()