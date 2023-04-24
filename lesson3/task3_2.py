name = input('enter name ')
surname = input('enter surname ')
year = int(input('enter year '))
city = input('enter city ')
email = input('enter email ')
telephone = input('input telephone ')
def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(name= 'Vera', surname = 'Tatarskikh', year = '1985',
              city = 'Moscow', email = 'wiktorovna@mail.ru',
              telephone = '8-123-45-67'))
