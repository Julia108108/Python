# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
#  отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите длину одной стороны шоколадки: '))
m = int(input('Введите длину другой стороны шоколадки: '))
k = int(input('Введите количество долек шоколадки, которые хотите отломить: '))

"""""
Чтобы отломить k долек, нужно, чтобы k было кратно m или n, т.е. 
k делится на m или n без остатка
"""""

if (k % m == 0) or ( k % n == 0):
    print('yes')
else:
    print('no')