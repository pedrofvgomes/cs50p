import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    if sys.argv[1].split('.')[-1].lower() not in ['jpg', 'png', "jpeg"] and sys.argv[2].split('.')[-1].lower() not in ['jpg', 'png', "jpeg"]:
        sys.exit('Invalid input') 

    if sys.argv[1].split('.')[-1].lower() in ['jpg', 'png', "jpeg"] and sys.argv[2].split('.')[-1].lower() in ['jpg', 'png', "jpeg"] and sys.argv[1].split('.')[-1].lower() != sys.argv[2].split('.')[-1].lower():
        sys.exit('Input and output have different extensions')

    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')
    
    shirt = Image.open('shirt.png')
    shirtsize = shirt.size

    boneco = ImageOps.fit(image, shirtsize)
    boneco.paste(shirt, shirt)

    boneco.save(sys.argv[2])

    
        
    
    

if __name__ == '__main__':
    main()