def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and len(s) in range(2,7) and s.isalnum():
        foundnumber = False
        for letter in s:
            if not foundnumber and letter == '0':
                return False
            if foundnumber and letter.isalpha():
                return False
            if letter.isnumeric():
                foundnumber = True
        return True
    return False

if __name__ == '__main__':
    main()