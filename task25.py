# Задача №25. Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split(

# Решение 1 
list_A = input('Введите символы через пробел: ').split()
result = {}
for i in list_A:
    result[i] = 0
for i in list_A:
    if result[i] == 0:
        print(i)
    else:
        print(f"{i}_{result[i]}")
    result [i] += 1

# Решение 2
s = ("a a a b c a a d c d d").split() # ыыодим строку и переводим ее в список
dict = {} # созд пуст словарь
for i in s: # перебираем эл-ты списка
    if i not in dict: # i - эл-т массива. Эта строка проверяет есть ли в словаре ключ i. Если его нет, то создается и счетчик с нуля начинается
        dict[i] = 0 # добав. индекс 0
        print(i, end=' ') # выводится сама буква i, т.к. она встретилась в 1 раз
    elif i in dict: # если же буква i есть в словаре, значит у нее уже есть ключ значение. Тогда просто к нему прибавляется 1 
        dict[i] += 1
        print(f'{i}_{dict[i]}', end=' ') #  выводится сам ключ и значение, кот к нему прикрепляется

# Решение 3
list = 'a a a b c a a d c d d'
list = list.replace(' ','') # удалили пробелы
print(list)
i, n, str = 0, len(list),''
while i < n:
    if list[:i].count(list[i]) == 0: str += f'{list[i]} '
    else: str += f'{list[i]}_{list[:i].count(list[i])} '
    i += 1
print(str)

# Решение 4
my_input = input('Введите строку--> ').split() # вводим строку и вводим для нее в-цию split
my_result = [] # создаем пустой список
my_dict = dict() # создаем пустой словарь
for i in my_input: # запускаем цикл по эл-ам списка my_input
    my_result.append(i) # добавляем значение my_result
    if i in my_dict: # делаем проверку - если i содержится в клбчах словаря my_dict,
        my_result.append('_' + str(my_dict[i])) # то в этом случае мы к только что доавленному значению добавляем нижнее подчерк_ и строкове значение из словаря по ключу i
        my_dict[i] += 1 # мы увеличиваем на 1 значение словаря
    else: # в противном случае, если у нас нет в слоавре значения с таким ключом
        my_dict[i] = 1 # мы добавл значение с таким ключом и кладем его равным 1
print(*my_result)

# Решение 5
list_input = input('Введите строку: ').split()
d = {i: 0 for i in set(list_input)}
for i in list_input:
    print(f'{i}_{d[i]}' if d[i] else f'{i}', end=' ')
    d[i] += 1

# Решение 6
arr = "a a a b c a a d c d d".split(" ")
result_arr = []

for index_chr in range(len(arr) - 1):
    count = arr[:index_chr].count(arr[index_chr])
    result_arr.append(f"{arr[index_chr]}_{count}" if count > 0 else f"{arr[index_chr]}")

Вот с помощью среза без дикта
print(" ".join(result_arr))