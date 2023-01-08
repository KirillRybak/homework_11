a = int(input("Введите число, которое делим  "))
b = "hello world"
try:
    c = a + b
except TypeError:
    print("Упс, что то пошло не так")
finally:
    print("Всё работает")


