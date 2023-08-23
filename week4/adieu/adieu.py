names = []

while True:
    try:
        names.append(input('Name: '))
    except EOFError:
        break

# caso 1
if len(names) == 1:
    print('Adieu, adieu, to ' + names[0])
# caso 2
if len(names) == 2:
    print('Adieu, adieu, to ' + names[0] + ' and ' + names[1])
# caso 3 e por ai fora
if len(names) > 2:
    result = 'Adieu, adieu, to ' + names[0] + ', '
    for name in names:
        if name != names[0] and name != names[-1]:
            result += name + ', '
    result += ' and ' + names[-1]
    print(result)