text = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
text = text.lower()
text = text.replace(' ', '')
if text == '42' or text == 'fortytwo' or text == 'forty-two':
    print('Yes')
else:
    print('No')