import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 1:
    fonts = figlet.getFonts()
    f = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] not in ['-f', '--font'] or sys.argv[2] not in figlet.getFonts():
        sys.exit('Invalid usage')
    f = sys.argv[2]
else:
    sys.exit('Invalid usage')

# definir fonte 
figlet.setFont(font=f)
s = input('Input: ')
print('Output: ' + figlet.renderText(s))