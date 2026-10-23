import datetime

year = 2021

monday = 0
for month in range(1,13):
    dt = datetime.datetime(year,month, 1)
    if dt.weekday() == 0:
        monday += 1
        print(dt.date())
