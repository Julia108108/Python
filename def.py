# Нужно создать ф-цию sumNumbers, которая будес считать сумму всех чисел от 1 до n
def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)
sum_numbers(5)

# переделаем ф-цию, чтобы она нам возрващала какое-то значение
def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
print('stop')

a = sum_numbers(5)
print(a)

# есть правило, что ф-ции и процедуры сколкьо принимает
# аругментов,с только и возращает. Но можно сделать так: смотри y = Hello
def sum_numbers(n, y = 'Hello'): # ввели 2-ю переменную y
    print(y) # можно вывести y по умолчанию
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
print('stop')

a = sum_numbers(5, 'qwerty') # если все-таки хотим передать значение y, то можем записать его сюда
print(a)

# напишем ф-цию, кот будет принимать неограниченное кол-во эл-ов
def sum_str(*args): # с пом * мы сообщаем пайтону, что хотим передать неогранич кол-во эл-ов
    res = ''
    for i in args: # создадим переменную res, которая имеет тип данных строка
        res += i
    return(res)
print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 'f'))
