# множества (set)

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()

# создадим множество
q = set()

# копирование одного мн-ва в другое
a = {1, 2, 3, 5, 8} # есть мн-во a
b = {2, 5, 8, 13, 21} # есть мн-во b
c = a.copy() # копиреум мн-во a в мн-во c
# выводится: c = {1, 2, 3, 5, 8}

# объединение мн-в
a = {1, 2, 3, 5, 8} # есть мн-во a
b = {2, 5, 8, 13, 21} # есть мн-во b
u = a.union(b) # мн-во u будет содержать уникальные значения из мн-в a и b
# выведется: u = {1, 2, 3, 5, 8, 13, 21}

# пересечение мн-в (т.е. те элементы, которые есть в обоих мн-ах)
a = {1, 2, 3, 5, 8} 
b = {2, 5, 8, 13, 21} 
i = a.intersection(b) # i = {8, 2, 5}

# найдем разность мн-ва a от мн-ва b ( a минус b, т.е. берем мн-во а и из него вычитаем все знач, кот. есть в мн-ве b)
a = {1, 2, 3, 5, 8} 
b = {2, 5, 8, 13, 21} 
dl = a.difference(b) # dl = {1, 3}

# найдем разность мн-ва b от мн-ва a 
a = {1, 2, 3, 5, 8} 
b = {2, 5, 8, 13, 21} 
dr = b.difference(a) # dr = {13, 21}

# функция
q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
# порядок действий:
# 1. a.intersection(b) - найдем пересечение a и b
# 2. a.union(b) - a объединяем с b.
# 3. a.union(b).difference(a.intersection(b)) - из полученного мн-ва находим разность с этим мн-ом

