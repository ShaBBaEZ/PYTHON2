# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

number = int(input("Введите количество элементов списка: \n"))
number_list = []
your_number = int(input("Введите число для поиска в списке: \n"))
for i in range(number):
    number_list.append(i + 1)
value = number_list[-1]
print(number_list)
print(your_number)
for i in number_list:
    if i == your_number:
        value = i + 1
print(value)


