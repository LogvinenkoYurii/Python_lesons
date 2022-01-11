import os

#Задание 1
# filename = "domains.txt"
#
#
# def get_domains(filename):
#     result_list = list()
#     with open(filename, "r") as domains:
#         data = domains.read()
#     data = data.split("\n")
#     for num in range(len(data)):
#         result_list.append(data[num].replace(".", ""))
#     return result_list
#
#
# result = get_domains(filename)
# print(result)


#Задание 2
# filename = "names.txt"
#
#
# def get_surname(filename):
#     res_list = list()
#     with open(filename, "r") as surname:
#         data = surname.read()
#     data = data.split("\t")
#     data.pop(0)
#     for num in range(len(data)):
#         if not num % 3:
#             res_list.append(data[num])
#     return res_list
#
# result = get_surname(filename)
# print(result)


#Задание 3
filename = "authors.txt"


def get_dict_date(filename):
    res_list1 = list()
    res_list2 = list()
    with open(filename, "r") as date:
        data = date.read()
    data = data.split("-")
    for num in range(len(data)):
        res = data[num].rfind("\n")
        res_list1.append(data[num][res::])
    for num in range(len(res_list1)):
        res_list2.append(res_list1[num][1::])
    return res_list2


result = get_dict_date(filename)
print(result)