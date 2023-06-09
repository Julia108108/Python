# 1. Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.
""""""
# Решение 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
i = 1

for i in a:
    if i < 5:
        print(i)

# Решение 2
print([elem for elem in a if elem < 5])
""""""

# 2. Даны списки: a и b. Нужно вернуть список, который состоит из элементов,
# общих для этих двух списков.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = set(a).intersection(b)
print(common)


# 3.Дан произвольный список. 
# Представьте его в обратном порядке.
my_list = [2, 4, 8]
print(my_list[::-1])

# другое решение:
my_list = [2, 4, 8]
my_list.reverse()
print(my_list)

