l = dict()
while True:
    try:
        item = input()
    except EOFError:
        for i in l.keys():
            print(str(l[i]) + ' ' + i.upper())
        break     