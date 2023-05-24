# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 
number = int(input("Введите натуральное число больше 1: "))
i = 3
fib_one = 0
fib_two = 1
answer = fib_one + fib_two
while answer <= number:
    fib_one = fib_two
    fib_two = answer
    answer = fib_one + fib_two 
    i += 1

print(answer)
if number == answer:
    print(i)
else:
    print(-1)



    не работает код