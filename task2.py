# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

a = int(input('Введите трёхзначное число: '))

figure1 = a % 10
a = a // 10
figure2 = a % 10
a = a // 10

print('Сумма цифр числа: ', a + figure1 + figure2)   