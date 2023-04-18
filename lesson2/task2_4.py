mas4 = input('Введите 5 слов через пробел ').split()
a = 1
for word in mas4:
    if len(word) > 10:
        print(f'{a}. {word[:10]}')
    else:
        print(f'{a}. {word}')
    a += 1
print()
