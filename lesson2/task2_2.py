mas2 = input('Введите 6 целых чисел через пробел ').split(' ')
a, b = 0, 1
while len(mas2) > b:
    mas2[a], mas2[b] = mas2[b], mas2[a]
    a +=2
    b +=2
print ('Обмен значений соседних элементов массива: '*mas2)


