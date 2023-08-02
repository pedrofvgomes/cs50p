def removespaces(s):
    for i in range(len(s)):
        if s[i] != ' ':
            return s[i:]

def main():
    g = input("Greeting: ")
    g = removespaces(g.lower())

    if g[0:5] == 'hello':
        print('$0')
        return

    if g[0] == 'h':
        print("$20")
        return

    print("$100")

main()