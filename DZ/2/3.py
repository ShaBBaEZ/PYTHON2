# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('Введите число: \n'))
i = 1
while i < number // 2:
    print (i * 2)
    i += 1