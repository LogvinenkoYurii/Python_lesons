#Задани 1
# num = int(input())
# num = str(num)
# result_num = num.count("0")
# print(result_num)


#Задание 2
# num = int(input())
# num = str(num)
# result_num = (len(num) - len(num.rstrip("0")))
# print(result_num)


# Задание 3
# my_list = ["qwe", "rty", "uio"]
# my_list_new = list()
# for num in range(len(my_list)):
#     my_list_new.append(my_list[num])
#     if num % 2:
#         my_list_new[num] = my_list_new[num][::-1]
# print(my_list_new)


#Задание 4
# my_list = [1, 2, 3, 4, 5]
# new_list  = list()
# for num in my_list[1:]:
#     new_list.append(num)
# new_list.append(my_list[0])
# print(new_list)


#Задание 5
# my_list = [1, 2, 3, 4]
# num = my_list.pop(0)
# my_list.append(num)
# print(my_list)


#Задание 6
# string = "43 больше чем 34 но меньше чем 56"
# item_list = list()
# resault = 0
# for item in string.split():
#     if item.isdigit():
#         item_list.append(item)
# for item in item_list:
#     resault += int(item)
# print(resault)


#Задание 7
# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
# first = my_str.find(l_limit)
# last = my_str.rfind(r_limit)
# sub_str = my_str[first+1: last]
# print(sub_str)


#Задание 8
my_str = "abcd"
resault = my_str[0::2]
print(resault)