from chartRip import getWeek
import datetime

def getMany(folder, url):
    year = int(input("Enter year: "))
    month = int(input("Enter month (no leftward 0): "))
    day = int(input("Enter day (no leftward 0): "))

    start = datetime.date(year, month, day)
    now = datetime.date.today()
    
    while str(start) <= str(now):
        getWeek(folder, url + "/" + str(start))
        start += datetime.timedelta(days=7)