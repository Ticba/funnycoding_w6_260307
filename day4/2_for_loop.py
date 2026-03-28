# range() function



R = range(0, 101, 1)
print(R)




# for loop


# 迴圈 -> 重複做區塊內的程式
'''

print(0)
print(1)
print(2)
..
print(100)
'''

# syntax
'''
var = 2
for 變數(var以外) in 數列(iterable):
    print(i)
'''

'''
iterable:
1. list
2. range()
'''
for i in range(0, 101):
    print(i)
    # 此區塊重複執行，i 從 0 開始一路變到 100


# 利用 for 迴圈輸出 0 2 4 .... 100