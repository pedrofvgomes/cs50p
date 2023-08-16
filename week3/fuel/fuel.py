### regras
# pedir input X/Y, ambos inteiros
# percentagem arredondada ao inteiro mais proximo de combustivel no deposito
# se for menos de 1%, E
# se for mais de 99%, F
### exceptions
# se X ou Y nao forem inteiros
# se X for maior que Y
# se Y for 0
### pedir input outra vez
# apanhar ValueError ou ZeroDivisionError

while True:
    try:
        f = input('Fraction: ')
        f = f.split('/')
        x = int(f[0])
        y = int(f[1])
        result = x/y * 100
    except (ValueError, ZeroDivisionError):
        continue
    else:
        if x<=y:
            break

if result < 1:
    result = 'E'
elif result > 99:
    result = 'F'
else:
    result = str(round(result)) + '%'

print(result)