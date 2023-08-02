def main():
    time = convert(input('What time is it? '))
    if time >= 7 and time <= 8:
        print('breakfast time')
    if time >= 12 and time <= 13:
        print('lunch time')
    if time >= 18 and time <= 19:
        print('dinner time')


def convert(time):
    time = time.split(':')
    return float(time[0]) + float(time[1])/60


if __name__ == "__main__":
    main()