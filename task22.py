# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2 
# 3 6 9 12 15 18
# 6 12

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
list_n = (input(f'Введите элементы первого множества n: ')).split()
list_m = (input(f'Введите элементы второго множества m: ')).split()
set_list_n = set(list_n)
set_list_m = set(list_m)
result_set = sorted(set_list_n.intersection(set_list_m))

# a = {i for i in set_list_n.intersection(set_list_m)}
# list_new = list(a)
# list_new.sort()

print(set_list_n)
print(set_list_m)
print(result_set)

"""
n = int(input("Введите количество элементов первого множества"))
m = int(input("Введите количество элементов второго множества"))

set_1 = set(int(input(f"Введите {n} элементов первого множества")) for _ in range(n))
set_2 = set(int(input(f"Введите {m} элементов второго множества")) for _ in range(m))
result_set = sorted(set_1.intersection(set_2))
print(set_1)
print(set_2)
print(result_set)
"""