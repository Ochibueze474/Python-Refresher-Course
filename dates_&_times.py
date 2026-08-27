
import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
print(date)
print(today)

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
print(time)
print(now)

today_datetime = now.strftime("%H:%M:%S %m:%d:%Y")
print(today_datetime)

target_datetime = datetime.datetime(2031, 1, 2, 12, 34, 0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("The target date has passed!")
else:
    print("The target date has not passed!")






