# Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.
"""
from collections import Counter
list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
counter_objects = Counter(list_1)
keys = counter_objects.keys()
num_values = len(keys)
print(num_values)
"""
list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
set = set(list_1)
num_values = len(set)
print(num_values)