
import time
from datetime import date
from datetime import timedelta


# get a list of timestamps at midnight for the last X days
def GetLastXDays(num_days):
  days = []
  i = 0
  while i < num_days:
    one_day = int(time.mktime((date.today() - timedelta(days = i)).timetuple()))
    days.append(one_day)
    i += 1

  days = sorted(days)
  return days
