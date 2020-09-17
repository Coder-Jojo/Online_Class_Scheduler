import csv
import webbrowser as web
import datetime as dt

with open('table.csv') as f:
    reader = csv.reader(f)
    table = list(reader)

a = dt.datetime.now()
print("the time right now is:", a.hour, a.minute)
x = dt.time(hour=a.hour, minute=a.minute)

#a,b,day = [int(t) for t in input().split()]
#x = dt.time(hour=a,minute=b)
hr = x.hour
time = (hr-8)*60 + x.minute - 25
cla = 0
if(time>=0 and time <= 90*6):
    cla = (time//90) + 1
    day = dt.datetime.today().weekday()
    if(table[day][cla] != ""):
        web.open(table[day][cla])
        exit()
    else:
        print("no class chill")
else:
    print("no class chill")



