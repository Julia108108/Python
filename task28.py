# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.
# Пример:
# 2 2
# 4

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

def sum(a, b):
    if (a > 0) and (b > 0):
        return (a + b)
    else:
        print('Введены неверные числа')
print(a + b)