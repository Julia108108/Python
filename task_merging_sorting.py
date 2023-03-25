# Сортировка слиянием

def merge_sort(nums): # nums - наш список
    if len(nums) > 1:
        mid = len(nums) // 2 # это бдует середина
        left = nums[:mid] # список для левой части от начала и до середины
        right = nums[mid:] # список для правой части от середины и до конца
        merge_sort(left) # теперь нужно делить наши списки до конца до конца, по ка не остануться оп 1 значению. Это можно сделать с пом рекурсии. сортируем левую часть 
        merge_sort(right)
        i = j = k = 0 # теперь нужно все эл-ты соединить воедино. создадим 3 переменных i j k
        while i < len(left) and j < len(right): #  в цикл будем класть эл-ты послеовательно. i для left, j для right. k - для итогового списка
            if left[i] < right[j]:
                nums[k] = left[i] # тут уже проверили элемент left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(list1)
print(list1)