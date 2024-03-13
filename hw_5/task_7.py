import datetime


def is_date(day, month, year):
    date = f"{day}{month}{year}"
    try:
        datetime.datetime.strptime(date, "%d%m%Y")
    except:
        return False

    return True


d = input("day: ")
m = input("month: ")
y = input("year: ")

print(is_date(d, m, y))

