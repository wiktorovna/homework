# 1
costs = 100
revenue = 200
profit = revenue - costs
print(profit)

cash = int(input('Введите сумму в кошельке '))
quantity = int(input('Сколько вы хотите пачек творога? '))
price = 50
purchase = quantity * price
change = cash - purchase
if cash >= purchase:
    print(f'Вы сможете купить {quantity} пачек творога, сдача = {change}')
else:
    print('Вашей суммы не хватит на покупку такого количества творога')
