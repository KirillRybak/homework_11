day = int(input("Введите день вашего рождения "))
month = int(input("Введите месяц рождения "))
years = int(input("Введите год рождения "))
day_now = int(input("Введите текущий день "))
month_now = int(input("Введите текущий месяц "))
years_now = int(input("Введите текущий год "))
s_years = years_now - years                  #число лет, без расчёта месяцев
s_month = month + month_now
if s_month >= 12:
    s_years = s_years - 1
print(s_years)