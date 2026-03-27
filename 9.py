def convert_datetime(datetime_str):
    """
    Converts date and time from MM/DD/YYYY HH:MM:SS format
    to seconds passed since the beginning of the year
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
        return None

    if month_num < 1 or month_num > 12:
        print("Ошибка: Неверный месяц.")
        return None

    if is_leap_year(year_num):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day_num < 1 or day_num > days_in_month[month_num - 1]:
        print("Ошибка: Неверный день для месяца")
        return None

    if year_num < 0 or year_num > 9999:
        print("Ошибка: Неверный год.")
        return None

    if hour_num < 0 or hour_num > 23:
        print("Ошибка: Неверный час.")
        return None

    if minute_num < 0 or minute_num > 59:
        print("Ошибка: Неверные минуты.")
        return None

    if second_num < 0 or second_num > 59:
        print("Ошибка: Неверные секунды.")
        return None

    days_passed = 0

    for i in range(month_num - 1):
        days_passed += days_in_month[i]

    days_passed += day_num - 1

    total_seconds = days_passed * 24 * 3600
    total_seconds += hour_num * 3600
    total_seconds += minute_num * 60
    total_seconds += second_num

    return total_seconds


def is_leap_year(year):
    """Checks if the year is a leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


user = input()
result = convert_datetime(user)

if result is not None:
    print(f"Количество секунд с начала года: {result}")
