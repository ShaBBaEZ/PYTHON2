# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
import random
from random import randint
my_list = []
for _ in range(10):
    my_list.append(random.randint(0,10))
print(my_list)
my_list = set(my_list)
print(my_list)
print(len(my_list))
