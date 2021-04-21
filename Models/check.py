import datetime
from datetime import date

weightloss_exercises = {'Forward Lunge': 0,
                    'Burpee': 0,
                    'Explosive Lunge': 0,
                    'Squat': 0,
                    'Double Jump': 0}
data = 'Forward Lunge'

weightloss_exercises[data] = weightloss_exercises[data]+1
for item in weightloss_exercises:
    print(item)

d1 = datetime.datetime.today().strftime("%Y-%m-%d")
data = d1.split("-")
date1 = date(int(data[0]), int(data[1]), int(data[2]))
print(date1)
d2 = datetime.datetime.today().strftime("%Y-%m-%d")
data1 = d2.split("-")
date2 = date(int(data1[0]), int(data1[1]), int(data1[2]))
print(date2)
print((date2-date1).days)

a=[1,52,45,7,5]

for i in range(len(a)-1):
    print(i, a[i], a[i+1])