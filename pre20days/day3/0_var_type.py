# 變數類型 int, float, string, bool, list, tuple, dict

# print(type(3))      # int
# print(type(3.0))    # float (有小數點)
# print(type(True))   # bool
# print(type('hello'))# str

# var1, var2, var3, var4 = 3, 3.0, True, 'hello'
# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))


print(type(1-1*5+3))    # 1*5 -> 5 (int) , 1-5 -> -4 (int), -4+3 -> -1 (int)
# int +/-/* int -> int

print(type(1*1.0))      # 1*1.0 -> 1.0 (float)
# int * float -> float
# int 與 float 透過算術運算子 (加減乘除...) -> float
# 相當於 print(type(1.0*1.0))

# 隱性轉換




# x = input()     # str
# x = int(x)      # 顯性轉換
# print(x+x)      # + 的左右放了什麼類型的資料，會決定他的運算方法
# # 1. int + int -> int (算數)
# # 2. str + str -> str (串接)


# 顯性轉換，強制轉換



# 字串

str1 = 'tab 換行'       # 可以直接輸出的文字

# 跳脫字元 '\'
# '\n' -> 換行,    \' -> '    \t -> tab鍵     \\ -> \ 符號
str2 = '\n\n'             #換行、tab鍵
str3 = '\t跳脫字元\'這是引號'
str4 = '\\O.O/'
# \O.O/

print(str1+str2+str3)
print(str4)