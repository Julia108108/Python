# быстрая сортировка

def quick_sort(array): # создаем ф-цию def quick_sort. В параметрах будем передавать массив array
    if len(array) <= 1: # если длина массива <=1
        return array # то мы возвращаем наш массив
    else: # иначе
        pivot = array[0] # создаем переменную pivot, в кот будем созранять наш 1 эл-т array[0]
    less = [i for i in array[1:] if i <= pivot] # создадим два массива less и greater. В 1 массив будем записывать те числа, кот
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater) # используем ф-цию quick_sort для сортировки двух списков

print(quick_sort([15, 5, 9, 6, 3, 58, 7, 5, 2, 7])) 
