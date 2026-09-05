# 讀取一行輸入
# var_input = input()
# print(var_input, end=' ')
# print(var_input)

# input("提示文字")
# var = input() # 1 -> 一次是讀取一行
"""var = input("請輸入你的名字：")
print("你的名字是")
print(var)"""

# 如果輸入是...
# 名字 年紀

'''
1. 一行
Alan 12


2. 兩行
Amy (press enter)
13

'''

# user_info = "Ticba 30 asdkjfl;asdlfj"
# user_info = input()             # 一整行當成一個字來看待
# a,b = user_info.split("b")      # split() 將一組字拆成多組字（預設空白）
# print(b)

# print(sep=" ")

# print("banana", "apple", 5)                 # 東西（變數/資料）
# print("banana", "apple", 5, sep=' ')        # 這行等同於上一行


# # 使用情況來觀察

# "你要切的字".split("切開的符號")             # 將字一分為多個
# print("apple", "banana", sep="分隔符號")    # 將要輸出的字中間插入「分隔符號」


# 例子：
# 輸入：
# 身高 體重 年齡
# 輸出：
# 身高///體重///年齡


"""input_message = input()         # 一行就是一個 input()
a,b,c = input_message.split()   # 將輸入切開存入三個變數箱子 a,b,c
print(a,b,c, sep="///")         # 將三個變數輸出，中間以分隔符號 /// 代替空白符號"""



# 練習題：
# 情境：30,40,100,90,80,70 前兩個數學、中間兩個中文、最後兩個英文
# 你希望拆成： 
# 30/40
# 100/90
# 80/70

# 輸入：30,40,100,90,80,70
# 輸出：
# 30/40
# 100/90
# 80/70


input_message = input()                 # 一行就是一個 input()
a,b,c,d,e,f = input_message.split(",")     # 將輸入切開，以","切開
print(a,b, sep="/")                     # 中間以分隔符號 "/" 代替空白符號
print(c,d, sep="/")                     # 中間以分隔符號 "/" 代替空白符號
print(e,f, sep="/")                     # 中間以分隔符號 "/" 代替空白符號