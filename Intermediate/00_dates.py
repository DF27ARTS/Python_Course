
### Dates ###

from datetime import datetime, time, date, timedelta


def print_date(date):
    print(date.date())
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


now = datetime.now()
print_date(now)

year_2024 = datetime(2024, 1, 1)
print_date(year_2024)


current_time = time(5, 35, 50)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


current_date = date.today()
print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(2024, 5, 20)
print(current_date.day)
print(current_date.month)
print(current_date.year)

current_date = date(current_date.year, current_date.month, current_date.day)
print(current_date)

diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)


start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(200, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
