# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
import random
my_list = [random.randint(0,10) for _ in range(20)]
print(my_list)

counter = {}

for item in my_list:
    counter[item] = counter.get(item,0) + 1
    if counter.get(item) < 2:
        print(item, end = ' ')
    else:
        print(str(item) + '_' + str(counter.get(item) - 1) , end = ' ')



        


