import random
#Задание 1
# l1 = []
# for _ in range(10):
#     l1.append(random.randint(1, 100))
# print(l1)
# l1 = tuple(l1)
# print(l1)


#Задание 2
# l1 = [(10, 20, 40,), (40, 50, 60,), (70, 80, 90,)]
# for i in range(len(l1)):
#     l1[i] = list(l1[i])
# for t in range(len(l1)):
#     l1[t][-1] = (100)
# for n in range(len(l1)):
#     l1[n] = tuple(l1[n])
# print(l1)
# print(type(l1))
# for r in range(len(l1)):
#     print(type(l1[r]))


#Задание 3
# tpl1 = (1, 2, 3, 4)
# tpl2 = (3, 5, 2, 1)
# tpl3 = (2, 2, 3, 1)
# resault = []
# for i in range(len(tpl1)):
#     resault.append(tpl1[i] + tpl2[i] + tpl3[i])
#     print(resault)
# tpl4 = tuple(resault)
# print(tpl4)


#Задание 4
# text = str(input("Введите текст: ")).lower()
# set1 = set()
# set1.update(text)
# if 'a' in set1:
#     print("Буква 'а' есть в наборе")
# else:
#     print("Буквы 'а' нет в наборе")


#Задание 5
# set1 = set()
# set2 = set()
#
# for _ in range(10):
#     set1.add(random.randint(1, 100))
# for _ in range(10):
#     set2.add(random.randint(1, 100))
# print(set1)
# print(set2)
# resault = set1.isdisjoint(set2)
# print(resault)


#Задание 6
# set1 = set()
# set2 = set()
#
# for _ in range(10):
#     set1.add(random.randint(1, 100))
# for _ in range(10):
#     set2.add(random.randint(1, 100))
# print(set1)
# print(set2)
# resault = set1.difference(set2)
# print(resault)


#Задание 7
# set1 = set()
# set2 = set()
#
# for num in range(10):
#     set1.add(random.randint(1, 100))
# for num1 in range(10):
#     set2.add(random.randint(1, 100))
# print(set1)
# print(set2)
# resault = set1.intersection(set2)
# for num in resault:
#     set1.remove(num)
# print(set1)


#Задание 8
# list1 = []
# list2 = []
# for _ in range(10):
#     list1.append(random.randint(1, 100))
# print(list1)
# for _ in range(10):
#     list2.append(random.randint(1, 100))
# print(list2)
# for item in list1:
#     if list2.count(item) == 0:
#         list2.append(item)
# print(list2)
# for num in list2:
#     if list2.count(num) == 2:
#         list2.remove(num)
# print(list2)
#