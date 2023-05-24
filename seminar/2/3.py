# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
# from random inport randint

from random import randint
count_water = int(input("Введите количество арбузов"))
min_water = float("inf") # + бесконечность
max_water = float("-inf") # - бесконечность
for i in range(count_water):
    weigth = randint(1,10)
    if weigth < min_water:
        min_water = weigth
    if weigth > max_water:
        max_water = weigth
print(min_water , max_water)




