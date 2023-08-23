def main():
    s = input('Input: ')
    print("Output: " + shorten(s))

def shorten(word):
    result = ""
    for c in word:
        if c.lower() not in ['a','e','i','o','u']:
            result += c
    return result

if __name__ == '__main__':
    main()