# За день машина проезжает n километров. Сколько дней нужно,
# чтобы проехать маршрут длиной m километров? При решении этой 
# задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output: 2

# Решение № 1
import math # библиотека math отвечает за математич операции
a = int(input('Введите количество километров в день: '))
b = int(input('Введите маршрут в км: '))
print(math.ceil((b / a)))


# Решение № 2
print((m := int(input())) // (n := int(input())) + (m % n > 0))

# Решение № 3
n = int(input())
m = int(input())
s = (m + n - 1) // n
print(s)

# Решение № 4
n = int(input('Введите сколкьо км машина проезжает за день:'))
m = int(input('Введите длину маршрута: '))

print(f'Чтобы проехать маршрут длиной {m} км нужно {int(((m + n) - 1) / n)} дня')