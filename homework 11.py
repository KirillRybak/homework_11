
try:
    a = int(input("Введите число, которое делим  "))
    b = "Hello"
    c = a + b
except TypeError:
    print("Упс, что то пошло не так")
except ValueError:
    print("И снова что то пошло не так")
finally:
    print("Всё работает")



