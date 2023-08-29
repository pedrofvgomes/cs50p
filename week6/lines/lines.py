import sys

def main():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')

    if sys.argv[1][-3:] != '.py':
        sys.exit('Not a python file') 

    lines = []
    opened = False
    with open(sys.argv[1], "r") as file:
        opened = True
        for line in file:
            lines.append(line.rstrip())

    if not opened:
        sys.exit('File does not exist')
    
    counter = 0
    for line in lines:
        comment = False
        first = True
        for character in line:
            if character == '#' and first:
                comment = True
            if character != ' ':
                first = False
        if not comment and not first:
            counter+=1

    print(counter)


if __name__ == '__main__':
    main()