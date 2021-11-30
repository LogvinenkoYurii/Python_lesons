# n = int(input("Среднее количество километров за день: "))
# m = int(input("Неообходимо проехать километров: "))
#
# if n >= m:
#     print(" 1 День")
# elif n <= 0 or m <= 0:
#     print("Incorrect input")
# else:
#     x = m//n
#     if m % n > 0:
#         x += 1
#     print(f"Необходимо дней : {x}")



# n = input("Введите трехзначное число: ")
# if len(n) != 3:
#     print("Неверное число!")
# else:
#     n = int(n)
#     n1 = n % 10
#     n = n // 10
#     n2 = n % 10
#     n3 = n // 10
#     print("Сумма цифр числа:", n1 + n2 + n3)



# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))
# number3 = int(input("Введите третье число: "))
# if number1 > number2:
#     winner = number1
# else:
#     winner = number2
# if number3 > winner:
#     maxnumber = number3
# else:
#     maxnumber = winner
# print(maxnumber)



# year = int(input("Введите год: "))
#
# if year % 400 == 0:
#     print(f"{year} високосный")
# elif year % 100 == 0:
#     print(f"{year} не високосный")
# elif year % 4 == 0:
#     print(f"{year} високосный")
# else:
#     print(f"{year} не високосный")



# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print("Число четное")
# else:
#     print("Число не четное")