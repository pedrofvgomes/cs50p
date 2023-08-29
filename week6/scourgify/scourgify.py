import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    if sys.argv[1][-4:] != '.csv' or sys.argv[2][-4:] != '.csv':
        sys.exit('Not a CSV file') 
    
    opened = False
    rows = []
    with open(sys.argv[1], "r") as file:
        opened = True
        for line in file:
            line = line.rstrip()
            if line != "name,house":
                name = ""
                first = ""
                last = ""
                house = ""
                name = line.split('"')[1]
                name = name.split(", ")
                first = name[1]
                last = name[0]
                house = line.split('"')[2][1:]

                row_data = {"first": first, "last": last, "house": house}
                print(row_data)
                rows.append(row_data)        

    with open(sys.argv[2], "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(rows)

    if not opened:
        sys.exit('File does not exist')
    

if __name__ == '__main__':
    main()