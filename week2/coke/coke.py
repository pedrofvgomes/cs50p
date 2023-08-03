current = 50
while current > 0:
    print("Amount Due: " + str(current))
    n = int(input("Insert Coin: "))
    if n == 5 or n == 10 or n == 25:
        current -= n
print("Change Owed: " + str(current*-1))