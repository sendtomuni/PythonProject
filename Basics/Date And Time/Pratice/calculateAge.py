import datetime

birthyear = datetime.datetime(1994,1, 5)

age = (datetime.datetime.now() - birthyear).days // 365

if (birthyear.month > datetime.datetime.now().month or
        (birthyear.month == datetime.datetime.now().month and
         birthyear.day > datetime.datetime.now().day)):
    print((datetime.datetime.now().year - birthyear.year)-1)
else:
    print((datetime.datetime.now().year - birthyear.year))
