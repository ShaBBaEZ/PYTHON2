# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
coin = int(input('Введите количество монет: \n'))
coin_eagle = 0
coin_tails = 0
for i in range(coin):
    coin_position = randint(0,1)
    print(coin_position)
    if coin_position == 0:
        coin_eagle += 1
    else:
        coin_tails += 1
if coin_eagle < coin_tails:
    print(coin_eagle)
else:
    print(coin_tails)
if coin_eagle == coin_tails:
    print(coin_tails)
