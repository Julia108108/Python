print(5, 8, 6)

n = 1.89
print(n)

n = 'abcd'
print(n)
n1 = "ahahahah"

m = 'agahahah'
print(type(m))

n = 'fd\'df' # чтобы вывести на печать кавычки нужен \
print(n)

"""          # это способ комментирования для целого куска текста
print(5, 8)
print(5)
print(5, 9)
"""

a = 5
b = 5.89
c = 'hello'

print(a, ' - ', b, ' - ', c) # это долго, вместо этого есть шаблон f-строки:

#шаблон f-строки
a = 5
b = 5.89
c = 'hello'

print(f"{a} - {b} - {c}")

#еще один шаблон
a = 5
b = 5.89
c = 'hello'

print("{} - {} - {}".format(a, b, c))

#ввод данных

# приглашаем ввести с новой строки
# print('Введите первую строку: ')
# a = input()

# приглашаем ввести в той же строке
# b = input('Введите второе число: ')

# напишем программу, которая будет выводить сумму чисел
#print(a, ' + ', b, " = ", a + b)

# Привидение типов
c = 5.89
print(c)
n = int(c)
print(n)
# выводится сначала 5.89, а потом 5. С пом функции int мы смогли привести тип данных float (т е переменную c) к целочисленному значению

с = 5.89
print(c)
print(type(c))
c = int(c)
print(c)
print(type(c))

# еще ф-ции приведения типов данных
c = 1
print(c)
print(type(c))
c = bool(c)
print(c)
print(type(c)) 

# округление чисел
a = 5.8997
b = 6.55858
print(a*b)
# результат получается длинным, сократим число до 3 знаков после запятой.
# для этого используем ф-цию round
print(round(a*b, 3)) 

# сокращенное присваивание
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5

# логические операции
a = 1 > 4
print(a) # выведется False

a = 1 < 4 and 5 > 2
print(a) # выведется True

a = 1 == 2 
print(a) # выведется False

a = 1 != 2
print(a) # выведется True

a = 'qwe'
b = 'qwe'
print(a == b) # выведется True

a = 1 < 3 < 5 < 10
print(a) # выведется True

# Условия
username = input('Введите имя: ')
if username == 'Фрэнк':
    print('Ура, это же пукающий ФРЭНК!')
elif username == 'Петр':
    print('Я так ждала тебя, Петр')
elif username == 'Петя':
    print('Петя - топ)')
else:
    print('Привет, ', username)

