import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall('^um\W', s, re.IGNORECASE)) + len(re.findall('\Wum\W', s, re.IGNORECASE)) + len(re.findall('\Wum\W?$', s, re.IGNORECASE)) + len(re.findall('^um$', s, re.IGNORECASE))


if __name__ == "__main__":
    main()