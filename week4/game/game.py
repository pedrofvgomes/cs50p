import random
while True:
    n = input('Level: ')
    if n.isnumeric() and n > 0:
        n = int(n)
        break
guess = random.choice(range(1,n+1))
while True:
    g = input('Guess: ')
    if g.isnumeric() and int(g) > 0:
        g = int(g)
        break

if g<guess:
    print('Too small!')
if g>guess:
    print('Too large!')
if g==guess:
    print('Just right!')