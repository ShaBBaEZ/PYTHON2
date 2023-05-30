# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint
number = int(input("Введите количество элементов списка: \n"))
number_list = []
your_number = int(input("Введите число для поиска в списке: \n"))
for i in range(number):
    number_list.append(randint(0,100))
print(number_list)
print(your_number)
count = 0
for i in range(number):
    if your_number == number_list[i]:
        count += 1
print(count)