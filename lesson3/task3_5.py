
def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите числа через пробел или нажмите q для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Общая сумма чисел = {sum_res}')
    print(f'Общая сумма всех введенных чисел =  {sum_res}')
my_sum()

