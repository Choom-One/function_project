from datetime import datetime

list_of_dates = ['2020-06-12', '2015-08-07', '1993-07-15', '1993-02-21', '1989-03-01']

list_of_dates = [datetime.strptime(date, '%Y-%m-%d') for date in list_of_dates]

print(min(list_of_dates))