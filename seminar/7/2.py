# Задача №51. Общее обсуждение
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
import random
print(values := [random.randint(0,10) for i in range(10)]) #Создаем список с рандомными значениями от 0-9

characteristic = lambda items: items % 2 #создаём функцию характеристику в данном случае проверяем чётность

def some_by(func, objects):
    for i in object:
        if object[i] 