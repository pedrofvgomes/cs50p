import emoji

s = input('Input: ')
result = ''
par = False
if s[0] == ':':
    par = True
s = s.split(':')
while '' in s:
    s.remove('')
for i in range(len(s)):
    if par and i%2==0 or not par and i%2==1:
        result+=emoji.emojize(':' + s[i] + ':')
    else:
        result+=s[i]
print("Output: " + result)