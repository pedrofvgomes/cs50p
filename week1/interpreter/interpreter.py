s = input('Expression: ')
s = s.split(' ')
x = int(s[0])
z = int(s[2])
if s[1] == '+':
    print(float(x+z))
if s[1] == '-':
    print(float(x-z))
if s[1] == '*':
    print(float(x*z))
if s[1] == '/':
    print(float(x/z))