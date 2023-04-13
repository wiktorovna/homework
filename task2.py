# 2
t = int(input('Введите время в секундах '))
ch = int(t / 3600)
m = int((t - ch * 3600) / 60)
s = int((t - ch * 3600) - m * 60)
print('{0:02d}:{1:02d}:{2:02d}'.format(ch, m, s))
