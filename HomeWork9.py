import random
import string



#Задание 1
# def change_list(first_list):
#     result_list = list()
#     for value in first_list:
#         if value.startswith("a"):
#             result_list.append(value)
#     return result_list
#
# list1 = ["asd", "rgt", "abg", "qqqwe"]
# list2 = change_list(list1)
#
# print(list2)


#Задание 2
# def change_list(first_list):
#     result_list = list()
#     for value in first_list:
#         if "a" in value:
#             result_list.append(value)
#     return result_list
#
# list1 = ["sad", "rgt", "bga", "aqqqwe"]
# list2 = change_list(list1)
#
# print(list2)


#Задание 3
# def change_list(first_list):
#     result_list = list()
#     for value in range(len(first_list)):
#         if type(first_list[value]) is str:
#             result_list.append(first_list[value])
#     return result_list
# #
#
# list1 = [1, 2, 3, "11", "22", 33, "one"]
# list2 = change_list(list1)
#
# print(list2)


#Задание 4
# def new_list(string):
#     result_list = list()
#     for idx in range(len(string)):
#         if string.count(string[idx]) == 1:
#             result_list.append(string[idx])
#     return result_list
#
#
# test_str = "qqweeerrty"
# result = new_list(test_str)
# print(result)


#Задание 5
# def match_in_strings(string1, string2):
#     list1 = list()
#     result_list = list()
#     for value in string1:
#         if list1.count(value) == 0:
#             list1.append(value)
#     for symbol in list1:
#         if symbol in string2:
#             result_list.append(symbol)
#     return result_list
#
# test_str1 = "qqwwerrttyy"
# test_str2 ="qweeeeeee123"
# result = match_in_strings(test_str1, test_str2)
# print(result)


#Задание 6
# def string_without_repetitions(string1, string2):
#     list1 = new_list(string1)
#     list2 = new_list(string2)
#     result_list = list()
#     for symbol in list2:
#         if symbol in list1:
#             result_list.append(symbol)
#     return result_list
#
#
# test_str1 = "qwwwwerrrrtyyyy"
# test_str2 = "qweeeeeeerty123"
# result = string_without_repetitions(test_str1, test_str2)
# print(result)


#Задание 7
# def create_email(names, domains):
#     name = random.choice(names)
#     domain = random.choice(domains)
#     num = random.randint(100, 1000)
#     laters = string.ascii_lowercase
#     random_string = "".join(random.choice(laters) for i in range(5))
#     my_email = f"{name}.{num}@{random_string}.{domain}"
#     return my_email
#
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(names, domains)
# print(e_mail)