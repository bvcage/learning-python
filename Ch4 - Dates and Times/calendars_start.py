#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the calendar module
import calendar

# TODO: create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2023, 2, 0, 0)
print(str)

# TODO: create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2023, 2)
print(str)

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for d in c.itermonthdays(2023, 2):
    print(d)
  
# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for m in calendar.month_name:
    print(m)

for d in calendar.day_name:
    print(d)

for m in calendar.month_abbr:
    print(m)

for d in calendar.day_abbr:
    print(d)

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2023, m)
    week1 = cal[0]
    week2 = cal[1]
    if week1[calendar.FRIDAY] != 0:
        meetday = week1[calendar.FRIDAY]
    else:
        meetday = week2[calendar.FRIDAY]
    print(calendar.month_name[m], meetday)
