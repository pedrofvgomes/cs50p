import sys
from tabulate import tabulate

def main():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')

    if sys.argv[1][-4:] != '.csv':
        sys.exit('Not a CSV file') 
    
    headers = []
    table = []
    first = True
    opened = False
    with open(sys.argv[1], "r") as file:
        opened = True
        for line in file:
            line = line.rstrip().split(',')
            cols = []
            for a in line:
                cols.append(a)
            if first:
                for col in cols:
                    headers.append(col)
                first = False
            else:
                row = []
                for col in cols:
                    row.append(col)
                table.append(row)

    if not opened:
        sys.exit('File does not exist')

    print(tabulate(table, headers, tablefmt="grid"))
    

if __name__ == '__main__':
    main()