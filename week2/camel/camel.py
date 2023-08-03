s = input("camelCase: ")
result = []
current = ""
for letter in s:
    if letter.islower():
        current += letter
    if letter.isupper():
        result.append(current + '_')
        current = letter.lower()
result.append(current)
print("snake_case: " + ''.join(result))