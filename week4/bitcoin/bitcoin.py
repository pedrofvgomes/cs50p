import requests, sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Missing command-line argument')
    elif len(sys.argv) > 2:
        sys.exit()
    else:
        if is_float(sys.argv[1]):
            n = float(sys.argv[1])
        else:
            sys.exit('Command-line argument is not a number')

    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        rate = r.json()['bpi']['USD']['rate']
        rate = ''.join(rate.split(','))
        print(f"${float(rate)*n:,.4f}")

            
    except requests.RequestException:
        sys.exit()

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
if __name__ == '__main__':
    main()