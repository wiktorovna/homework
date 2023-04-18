

my_ratings = [9, 5, 3, 2, 2]
while True:
    value = input('Введите рейтинг - целое число  ("q" для завершения):')
    if value == "q":
        break
    value = int(value)

    i = my_ratings.count(value)

    for element in my_ratings:
        if i > 0:
            k = my_ratings.index(value)
            my_ratings.insert(k + i, value)
            break
        else:
            if value > element:
                l = my_ratings.index(element)
                my_ratings.insert(l, value)
                break
            elif value < my_ratings[len(my_ratings) - 1]:
                my_ratings.append(value)

    print(my_ratings)





