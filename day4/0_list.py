# What is list? collection of datas

empty_list = []             # empty list

list_1 = ['hi', 'ssssss']   # length is 2 

# var1 = 'hi'
# var2 = 'sssss'

print(list_1[0], list_1[1]) # indexing (accessing)     syntax: list_name[index]


# len() function   ->    檢驗一個複雜的資料的長度
# syntax len(datas)
print(len(empty_list))    


# negative index
print(list_1[-1])


# index out of range
# print(list_1[-5])   
    # list_1: 0, 1(positive) = len(list_1)-1    長度 - 1
    # list_1: -1, -2 (negative) = -len(list_1)  負的長度


# list 裡面可以放什麼資料？ all

list_2 = ["hello", 123, 1.0, [100, 200]]
# 想取到 "hello"
print(list_2[0])
print(list_2[1])
print(list_2[2])
print(list_2[3][0])





# list 的操作方式
# 把 1 ~ 100 加入空 List

# method1: 要加入資料的list.append(要加入的資料)

list_3 = []
# print(list_3)
# list_3.append(1)
# print(list_3)
# list_3.append(2)
# print(list_3)
# list_3.append(3)
# print(list_3)

for i in range(1,101):
    list_3.append(i)

print(list_3)



















