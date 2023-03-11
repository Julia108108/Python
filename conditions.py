#цикл while
n = 423 
summa = 0
while n > 0:
    x = n % 10 # остаток от деления на 10, это 3
    summa = summa + x
    n = n // 10 # делим наше число на 10, целочисленно. Это 42
print(summa) # сумма = 4 + 2 +3 = 9

# метод break
i = 0
while i < 5:
    if i == 3: # если i будет равняться 3, то мы выходим из цикла
        break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит )')
print(i)
# нежелательно использовать break, есть замена:

# метод флажок
n = int(input())
flag = True # цикл while будет выолнять до тех пор, пока flag равно true
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False # то мы меняем нашу переменную flag на False и наш цикл завершает свою раюоту
        print(i)
    elif i > n // 2: #
        print(n)
        flag = False
    i += 1


# функция range
range(100, 0, -20)
for i in range:
    print(i) # 100 80 60 40 20

a = 'qwerty'

print(a(0))