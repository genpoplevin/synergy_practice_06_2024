from datetime import datetime as dt
from utils import FIGURES, WEEK_DAYS

def get_birth_day():
    try:
        day = int(input("Введите день вашего рождения: "))
        if 1 <= day <= 31:
            return day
        else:
            print("День вашего рождения должен быть в диапазоне от 1 до 31")
            get_birth_day()
    except ValueError:
        print("День вашего рождения должен быть числом")
        get_birth_day()

def get_birth_month():
    try:
        month = int(input("Введите месяц вашего рождения в числовом формате: "))
        if 1 <= month <= 12:
            return month
        else:
            print("Месяц вашего рождения должен быть в диапазоне от 1 до 12")
            get_birth_month()
    except ValueError:
        print("Месяц вашего рождения должен быть числом")
        get_birth_month()

def get_birth_year():
    try:
        year = int(input("Введите год вашего рождения: "))
        if 1 <= year <= dt.now().year:
            return year
        else:
            print(f"Год вашего рождения должен быть в диапазоне от 1 до {dt.now().year}")
            get_birth_year()
    except ValueError:
        print("Год вашего рождения должен быть числом")
        get_birth_year()

def get_week_day(day, month, year):
    day = dt(year, month, day).weekday()
    return WEEK_DAYS[day]

def is_leap(year):
    if year %4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return "високосный"
    else:
        return "невисокосный"

def calculate_age(day, month, year):
    today = dt.now()
    born = dt(year, month, day)
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def print_age(n):
    if (n % 10 == 1) and (n % 100 != 11):
        return f"Вам {n} год."
    elif (n % 10 in (2, 3, 4)) and (n // 10 != 1):
        return f"Вам {n} года."
    else:
        return f"Вам {n} лет."

def print_birthday(day, month, year):
    day_t = day // 10
    day_o = day % 10
    month_t = month // 10
    month_o = month % 10
    year_th = year // 1000
    year_h = year // 100 % 10
    year_t = year // 10 % 10
    year_o = year % 10
    for i in range(11):
        print(FIGURES[day_t][i], ' ', FIGURES[day_o][i], '   ',
              FIGURES[month_t][i], ' ', FIGURES[month_o][i], '   ',
              FIGURES[year_th][i], ' ', FIGURES[year_h][i], ' ',
              FIGURES[year_t][i], ' ', FIGURES[year_o][i])

def main():
    print("Программа, которая по дню, месяцу и году вашего "
          "рождения определяет некоторые факты.")
    day = get_birth_day()
    month = get_birth_month()
    year = get_birth_year()
    week_day = get_week_day(day, month, year)
    print(f"День недели вашего рождения: {week_day}")
    print(f"Год вашего рождения {is_leap(year)}")
    print(print_age(calculate_age(day, month, year)))
    print("Дата вашего рождения:")
    print_birthday(day, month, year)

if __name__ == '__main__':
    main()