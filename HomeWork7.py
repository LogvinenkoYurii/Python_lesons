# Задани 1
num = int(input())
num = str(num)
result_num = num.count("0")
print(result_num)


# Задание 2
num = int(input())
num = str(num)
result_num = (len(num) - len(num.rstrip("0")))
print(result_num)


# Задание 3
my_list = ["qwe", "rty", "uio"]
my_list_new = list()
for num in range(len(my_list)):
    my_list_new.append(my_list[num])
    if num % 2:
        my_list_new[num] = my_list_new[num][::-1]
print(my_list_new)


# Задание 4
my_list = [1, 2, 3, 4, 5]
new_list  = list()
for num in my_list[1:]:
    new_list.append(num)
new_list.append(my_list[0])
print(new_list)


# Задание 5
my_list = [1, 2, 3, 4]
num = my_list.pop(0)
my_list.append(num)
print(my_list)


# Задание 6
string = "43 больше чем 34 но меньше чем 56"
item_list = list()
resault = 0
for item in string.split():
    if item.isdigit():
        item_list.append(item)
for item in item_list:
    resault += int(item)
print(resault)


# Задание 7
my_str = "My long string"
l_limit = "o"
r_limit = "g"
first = my_str.find(l_limit)
last = my_str.rfind(r_limit)
sub_str = my_str[first+1: last]
print(sub_str)


#Задание 8
my_str = "qwert"
res_list = list()
if len(my_str) % 2:
    my_str = my_str + "_"
for idx in range(0, len(my_str), 2):
    res_list.append(my_str[idx: idx +2])
print(res_list)


#Задание 9
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
result = 0
for idx in range(1, len(my_list)-1):
    if my_list[idx] > my_list[idx-1] + my_list[idx+1]:
        result += 1
print(result)


#Задание 10
persons = [{"name": "John", "age": 15},
           {"name": "Anna", "age": 23},
           {"name": "Dan", "age": 5},
           {"name": "Maximusss", "age": 24},
           {"name": "Olgha", "age": 25},
           {"name": "Volodymyr", "age": 5},
           {"name": "Jack", "age": 45}]
age = list()
name = list()

min_ages = list()
max_len_names = list()
for item in persons:
    age.append(item["age"])
    name.append(item["name"])
min_age = min(age)
max_name = max(name)

for chosen_persons in persons:
    if len(chosen_persons["name"]) == len(max_name):
        max_len_names.append(chosen_persons["name"])
    if chosen_persons["age"] == min_age:
        min_ages.append(chosen_persons["age"])

mean_age = int(sum(age) / len(age))
print(min_ages)
print(max_len_names)
print(mean_age)