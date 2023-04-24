def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c

print(f'Сумма двух наибольших чисел =  {my_func(int(input("введите 1 число ")),int(input("введите 2 число ")), int(input("введите 3 число ")))}')
