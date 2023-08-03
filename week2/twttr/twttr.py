s = input("Input: ")
result = ""
for letter in s:
    if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
        result += letter
print("Output: " + result)