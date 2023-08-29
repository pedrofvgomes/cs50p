import re
import sys


def main():
    a = convert(input("Hours: "))
    print(a)


def convert(s):
    s = s.strip()
    if re.search('^1?[0-9](:[0-9][0-9])? (AM|PM) to 1?[0-9](:[0-9][0-9])? (AM|PM)$', s):
        first, second = s.split(' to ')
        first = first.split(' ')
        second = second.split(' ')

        #### first
        # horas com :
        if ':' in first[0]:
            first1, first2 = first[0].split(':')
            if int(first1) >= 1 and int(first1) <= 12 and int(first2) >= 0 and int(first2) <= 59:
                if first[1] == 'PM':
                    start = str(int(first1) + 12) + ':' + first2
                else:
                    start = first1 + ':' + first2
            else:
                raise ValueError
        # horas inteiras
        else:
            if int(first[0]) >= 1 and int(first[0]) <= 12:
                if first[1] == 'PM':
                    start = str(int(first[0]) + 12) + ':00'
                else:
                    start = first[0] + ':00'
            else:
                raise ValueError


        #### second
        # horas com :
        if ':' in second[0]:
            second1, second2 = second[0].split(':')
            if int(second1) >= 1 and int(second1) <= 12 and int(second2) >= 0 and int(second2) <= 59:
                if second[1] == 'PM':
                    end = str(int(second1) + 12) + ':' + second2
                else:
                    end = second1 + ':' + second2
            else:
                raise ValueError
        # horas inteiras
        else:
            if int(second[0]) >= 1 and int(second[0]) <= 12:
                if second[1] == 'PM':
                    end = str(int(second[0]) + 12) + ':00'
                else:
                    end = second[0] + ':00'
            else:
                raise ValueError

        if re.search('^[1-9]:', start):
            start = '0' + start
        if re.search('^[1-9]:', end):
            end = '0' + end

        if start == '12:00':
            start = '00:00'
        if start == '24:00':
            start = '12:00'
        if end == '12:00':
            end = '00:00'
        if end == '24:00':
            end = '12:00'
        return start + ' to ' + end
    else:
        raise ValueError



if __name__ == "__main__":
    main()