# function 函式

# built-in 
# print()
# input()
# map()
# sum()
# max()
# min()

# self define
def wash_hands():
    # 你要怎麼「設計」 wash_hands 的功能
    print('濕')
    print('搓')
    print('沖')
    print('捧')
    print('擦')
    a = 1       # 區域變數 local variable
    print(a)
    global b
    print(b+1)

# call fucntion


print("day1")
wash_hands()
print("day2")
wash_hands()
a=2             # 全域變數 global variable
print(a)



# function 就是打包一些功能成一個設計圖