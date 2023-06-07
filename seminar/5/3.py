# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

num = int(input("Введите число: "))

# def prime_number(a):
#     kol = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             kol += 1
#     if kol == 2:
#         return(f"Число {num} простое")
#     else:
#         return(f"Число {num} составное")
    
# print(prime_number(num))

def is_simple(number: int) -> bool:
    if number in [1,2]:
        return True
    if number % 2 == 0:
        return False
    for dev in range(3,number //2 + 1, 2):
        if number % dev == 0:
            return False
    return True
        
print(is_simple(num))
