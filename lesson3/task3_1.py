def my_func(a, b):
    try:
        z = a / b
        return z
    except ZeroDivisionError:
        return "b не может быть = 0"
print(my_func(int(input("Введите a = ")), int(input("Введите b = "))))

