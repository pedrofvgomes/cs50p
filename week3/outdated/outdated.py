months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input('Date: ')
    # remove leading spaces
    newdate = ""
    started = False
    for i in range(len(date)//2):
        if date[i].isalnum():
            started = True
        if started:
            newdate += date[i]
    started = False
    appendix = ""
    for i in reversed(range(len(date)//2, len(date))):
        if date[i].isalnum():
            started = True
        if started:
            appendix += date[i]
    for i in reversed(range(len(appendix))):
        newdate += appendix[i]
    date = newdate
    if date.count('/') == 2:
        date = date.split('/')
        if date[0].isnumeric() and date[1].isnumeric() and date[2].isnumeric():
            m = int(date[0])
            d = int(date[1])
            y = int(date[2])
            if d in range(1,32) and m in range(1,13):
                break
    else:
        date = date.split(' ')
        if date[0] in months and date[1][-1] == ',' and date[1][0:-1].isnumeric() and date[2].isnumeric():
            d = int(date[1][0:-1])
            m = 0
            for month in months:
                if month == date[0]:
                    m = m + 1
                    break
                else:
                    m+=1
            y = int(date[2])
            if d in range(1,32) and m in range(1,13):
                break

print(f"{y:04}" + '-' + f"{m:02}" + '-' + f"{d:02}")