# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
from string import punctuation # модуль пунктуации. Лежат все знаки припинания


text = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells"""
for ch in punctuation:
    text = text.replace(ch, '') # прошлись по тексту и заменили все знаки припинания на ничего
text = text.lower()# превращаем строку в нижний регистр
text = text.split()# разделяем каждое слово по пробелу и делаем из строки список(АКА массив)
text = set(text)# выдаём только уникальные значения
print(len(text))# считаем кол-во элементов в списке
