import datetime

dateString = '05-01-1994'

dt = datetime.datetime.strptime(dateString, '%d-%m-%Y')
print(dt)