try:
    years = int(input("Введите год рождения"))
    years_now = int(input("Введите текущий год"))
    age_years = years_now - years
    month = int(input("Введите месяц рождения"))
    month_now = int(input("Введите текущий месяц"))
    age_month = month_now - month
    day = int(input("Введите день рождения"))
    day_now = int(input("Введите текущий день"))
    age_day = day_now - day
    if month > month_now:
        age_years = age_years - 1
    elif day > day_now:
        age_years = age_years - 1
    print(age_years)
except ValueError:
    print("Упс, что то пошло не так")