def main():
    g = input("Greeting: ")
    for i in range(len(g)):
        if g[i] != ' ':
            g = g[i:]
            break
    val = value(g.lower())
    print("$" + str(val))

def value(greeting):
    if greeting[0:5] == 'hello':
        return 0

    if greeting[0] == 'h':
        return 20

    return 100
if __name__ == '__main__':
    main()