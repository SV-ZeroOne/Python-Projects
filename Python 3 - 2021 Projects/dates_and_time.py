'''
Working with Dates and Time
'''

import datetime

# Todays date
today = datetime.date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)

create_day = datetime.date(2022, 3, 4)
print(f'My next birthday is: {create_day}' )

# How close to end of this year?
new_year = datetime.date(2022, 1, 1)
days_remaning = new_year - today
print(f'Days remaning of this year: {days_remaning.days}')

time = datetime.date.time(1,2,44,100)
print(time)
date_time = datetime.datetime(2020,1,22,12,44,12,10000)
print(date_time)

# Move forward withtime delta
time_delta = datetime.timedelta(days=10)
print(date_time + time_delta)

# Convert string date to date object
date_string = '2020-12-04'
date_object = datetime.date.fromisoformat(date_string)
print(date_object)