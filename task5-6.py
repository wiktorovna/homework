revenue = int(input('Введите значение выручки '))
costs = int(input('Введите значение издержек '))
profit = revenue - costs
ren = profit / revenue
if revenue > costs:
    print(f'Ваша прибыль {profit}')
    print(f'Ваша рентабельность {ren}')
elif revenue == costs:
    print('Ваша прибыль = 0')
    print(f'Ваша рентабельность {ren}')
else:
    print(f'Ваш убыток= {profit}')
number = int(input('Введите численность сотрудников '))
profit_number = profit / number
print(f'Ваша прибыль в расчете на 1 сотрудника =  {profit_number}')
