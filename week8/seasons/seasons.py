from datetime import date, datetime
import inflect
import re
import sys


def main():
    d = input('Date of Birth: ')
    if convert(d) != None:
        print(convert(d))
    else:
        sys.exit('Invalid date')
    

def convert(d):
    if not re.search('^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$', d):
        return None
    else:
        year, month, day = d.split('-')
        today = date.today()
        a = datetime(int(year), int(month), int(day), 0, 0, 0)
        b = datetime(today.year, today.month, today.day, 0, 0, 0)
        n = (b-a).total_seconds() / 60
        n = int(n)
        
        p = inflect.engine()
        return p.number_to_words(n, andword='').capitalize() + ' minutes'



if __name__ == "__main__":
    main()