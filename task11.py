# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи 
# оно является, то есть выведите такое число n, что φ(n)=A. Если А не является
# числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# Решение 1
i = int(input())
count = 2
prevNum = 0
nextNum = 1
while i >= nextNum:
    if nextNum == 1:
        print(count)
        break
    prevNum, nextNum = nextNum + prevNum
    count = count + 1
else:
    print(-1)



# Решение 2
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
number = int(input("Введите число: "))
f1 = f2 = 1
n = 3 # число больше 1
while number > f2:
    f1, f2 = f2, f1 + f2
    n +=1
print(n if number == f2 else '-1')

# Решение 3
a = int(input('Введите число: '))
first = 0
second = 1

if a == 0:
    print(1)
elif a == 1:
    print(2)

count = 2
while second < a:
    buffer=first+second
    first = second
    second = buffer
    count = count +1

if second == a:
    print(count)
else:
    print(-1)