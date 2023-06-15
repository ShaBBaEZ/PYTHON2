# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
from random import randint

my_list = [randint(0,10) for i in range (15)]
print(my_list)                                                                                                                                                                                                                                                                                                                             
count = 0
for i in range(1, len(my_list) - 1):
    if my_list[i - 1] < my_list[i]> my_list[i + 1]:
        count += 1
if my_list[-1] < my_list[0] > my_list[1]:
    count += 1
elif my_list[0] < my_list[-1] > my_list[-2]:
    count += 1
print(count)