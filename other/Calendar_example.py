import calendar
c = calendar.TextCalendar()
# print(c.formatyear(2022))
for d in c.monthdayscalendar(2022, 12):
    print(d)
