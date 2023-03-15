d = {}      # создаем пустой словарь
d = dict()  # создаем пустой словарь

d['q'] = 'qwerty'        # добавляем значения c помощью ключа q
print(d)

d['w'] = 'werty'        
print(d['q'])

# пример
dictionary = {}
dictionary = {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}

# можем выводить значения по ключу
print(dictionary['left'])   # ←

# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐

print(dictionary['type']) # KeyError: 'type'

del dictionary['left'] # удаление элемента

dictionary = {}
dictionary = {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
for item in dictionary: 
    print(item)
# выведутся:
# up
# down
# right


dictionary = {}
dictionary = {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
for item in dictionary: 
    print('{}: {}'.format(item, dictionary[item]))
# выведутся:
# up: ↑
# down: ↓
# right: →

dictionary = {}
dictionary = {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
for (k, v) in dictionary.items(): 
    print(k, v)
# выведутся:
# up: ↑
# down: ↓
# right: →

dictionary = {}
dictionary = {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary.items())
# выводится список, где каждый элемент будет ялв кортежем из 2 значений (ключ и значение из словаря)
# dict_items([('up':'↑'), ('left':'←'), ('down':'↓'), ('right':'→')])


