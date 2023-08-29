import re
import sys

def main():
    print(parse(input('HTML: ')))

def parse(s):
    s = s.strip()
    try:
        first, second = s.split('src=')
        second = second.split('"')
        url = second[1]
    except ValueError:
        return None
    
    if re.search(r"^(http|https)://(www.)?youtube.com/embed/+", url):
        lixo, url = url.split('embed/')
        return "https://youtu.be/" + url
        
    return None
    


if __name__ == '__main__':
    main()

