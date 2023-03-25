# Задача №29. Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга
# оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью
# товарищи обратились к Вам, студентам. Примечание: Программные коды на следующих слайдах
"""
Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)

Петя:
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n)
"""

# Решение 1
import random
numb = int(input('-->'))
max_number = 0
while numb != 0:
    if max_number < numb:
        max_number = numb
    numb = int(input('-->'))
print(max_number)

# Решение 2
arr = []
num = int(input("введите число "))
while(num!=0):
    arr.append(num)
    num = int(input("введите число "))
print(max(arr))

# Решение 3
i = int(input("Введите число: "))
maxN = i
while i != 0:
    i = int(input("Введите число: "))
    if i > maxN:
        maxN = i
print(maxN)

# Решение 4
maxN = 0
while (i := int(input())) or i != 0:
    if i > maxN:
        maxN = i
print(maxN)

