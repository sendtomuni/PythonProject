import datetime

today_day = datetime.datetime.now().weekday()

if today_day-3 >= 0:
    print((datetime.datetime.now() - datetime.timedelta(days=(today_day-3))).date())
else:
    print((datetime.datetime.now() - datetime.timedelta(days=(7-(3- today_day)))).date())