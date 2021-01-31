"""
ID: jyhome31
LANG: PYTHON3
TASK: friday
"""
fin = open('friday.in', 'r')
fout = open('friday.out', 'w')
N = int(fin.readline())
month = 1
day = 1
year = 1900
dayOfWeek = 1
dayList = [0, 0, 0, 0, 0, 0, 0]
for i in range(0, N):
    month = 0
    day = 0
    year = 1900 + i
    for j in range(0, 12):
        day = 0
        month = month + 1
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            for k in range(0, 31):
                day = day + 1
                dayOfWeek = dayOfWeek + 1
                if dayOfWeek > 6:
                    dayOfWeek = 0
                if day == 13:
                    dayList[dayOfWeek] = dayList[dayOfWeek] + 1
        if month == 4 or month == 6 or month == 9 or month == 11:
            for k in range(0, 30):
                day = day + 1
                dayOfWeek = dayOfWeek + 1
                if dayOfWeek > 6:
                    dayOfWeek = 0
                if day == 13:
                    dayList[dayOfWeek] = dayList[dayOfWeek] + 1
        if month == 2:
            if year%4 != 0:
                for k in range(0, 28):
                    day = day + 1
                    dayOfWeek = dayOfWeek + 1
                    if dayOfWeek > 6:
                        dayOfWeek = 0
                    if day == 13:
                        dayList[dayOfWeek] = dayList[dayOfWeek] + 1
            else:
                if year%100 == 0 and year%400 == 0:
                    for k in range(0, 29):
                        day = day + 1
                        dayOfWeek = dayOfWeek + 1
                        if dayOfWeek > 6:
                            dayOfWeek = 0
                        if day == 13:
                            dayList[dayOfWeek] = dayList[dayOfWeek] + 1
                elif year%100 == 0 and year%400 != 0:
                    for k in range(0, 28):
                        day = day + 1
                        dayOfWeek = dayOfWeek + 1
                        if dayOfWeek > 6:
                            dayOfWeek = 0
                        if day == 13:
                            dayList[dayOfWeek] = dayList[dayOfWeek] + 1
                else:
                    for k in range(0, 29):
                        day = day + 1
                        dayOfWeek = dayOfWeek + 1
                        if dayOfWeek > 6:
                            dayOfWeek = 0
                        if day == 13:
                            dayList[dayOfWeek] = dayList[dayOfWeek] + 1
endString = ""
for a in range(0, 6):
    endString += str(dayList[a]) + " "
endString += str(dayList[6]) + "\n"
fout.write(endString)
fout.close()
