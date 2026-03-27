def convert_datetime(datetime_str):
    """
    Converts date and time from MM/DD/YYYY HH:MM:SS format
    to DD.MM.YY HH:MM:SS format in 12-hour clock with AM/PM
    """
    try:
        date_part, time_part = datetime_str.split()

        month, day, year = date_part.split('/')

        hour, minute, second = time_part.split(':')

        month_num = int(month)
        day_num = int(day)
        year_num = int(year)
        hour_num = int(hour)
        minute_num = int(minute)
        second_num = int(second)

    except:
        print("Ошибка: Неверный формат строки")
        return

    if month_num < 1 or month_num > 12:
        print("Ошибка: Неверный месяц.")
        return

    if is_leap_year(year_num):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day_num < 1 or day_num > days_in_month[month_num - 1]:
        print("Ошибка: Неверный день для месяца")
        return

    if year_num < 0 or year_num > 9999:
        print("Ошибка: Неверный год.")
        return

    if hour_num < 0 or hour_num > 23:
        print("Ошибка: Неверный час.")
        return

    if minute_num < 0 or minute_num > 59:
        print("Ошибка: Неверные минуты.")
        return

    if second_num < 0 or second_num > 59:
        print("Ошибка: Неверные секунды.")
        return

    if hour_num == 0:
        hour_12 = 12
        period = "AM"
    elif hour_num < 12:
        hour_12 = hour_num
        period = "AM"
    elif hour_num == 12:
        hour_12 = 12
        period = "PM"
    else:
        hour_12 = hour_num - 12
        period = "PM"

    year_short = year_num % 100

    print(f"{day_num:02}.{month_num:02}.{year_short:02} "
          f"{hour_12:02}:{minute_num:02}:{second_num:02} {period}")


def is_leap_year(year):
    """Checks if the year is a leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


user = input()
convert_datetime(user)
