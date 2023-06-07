# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
import random
mark = []
n = int(input("Введите кол-во оценок: "))
for _ in range(n):
    mark.append(random.randint(1,5))

def min(array):
    min = array[0]
    for i in range(len(array)):
        if min > array[i]:
            min = array[i]
    return min

def max(array):
    max = array[0]
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]
    return max

min_mark = min(mark)
max_mark = max(mark)

def zamena(array):
    for i in range(len(array)):
        if array[i] == max_mark:
            array[i] = min_mark
    return array

print(min(mark))
print(max(mark))
print(mark)
print(zamena(mark))


# mark = [5,5,4,5,3,2,1,4]
# print(mark)
# maximal = max(mark)
# minimal = min(mark)
# for i in range(len(mark)):
#     if mark[i] == maximal:
#         mark[i] = minimal
# print(mark)
