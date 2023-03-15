t = ()  # создаем пустой кортеж
print(type(t))

t = (1, ) # при создании кортежа нужно обязат оставить запятую
print(type(t))

# преобразуем список в кортеж
v = [1, 8, 9] # вводим список
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

# разъединим кортеж на 3 переменные
v = tuple(v)
print(v)
print(type(v))

# a = 1 
# b = 2
# или присваивание можно сделать так: 
# a, b = 1, 2
# а если обе переменные равны 1, то можно записать так:
# a = b = 1

a,b,c = v

print(a, b, c)

# как выести элемент из кортежа:
t = (1, 2, 3, 5)
print(t[1]) # выведется 2-ой элемент, это 2

# с пом цикла for можно пройтись по всем эл-ам
t = (1, 2, 3, 5)
for i in t:
    print(i)

# и по-другому:
t = (1, 2, 3, 5)
for i in range(len(t)):
    print(t[i])

# изменим какой-то элемент
t = [1, 2, 3, 5]
t[0] = 2 # элементу с индексом [0] присваиваем значение 2
print(t)
