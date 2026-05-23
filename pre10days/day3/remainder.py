# 延伸
# 判斷 2 的倍數

# i = 2
# if i % 2 == 0:
#     print("even")
# else:
#     print("odd")


# 判斷 3 的倍數  -> 

i = 3
if i % 3 == 0:
    print('3k')
elif i % 3 == 1:
    print('3k+1')
else:
    print('3k+2')


# 特例：10 的倍數
# 13847190234 % 10 -> 個位數 (ones) = 4,   
# 13847190234 // 10 -> 除了個位數的其他數 = 1384719023

x = 153 
print(x % 10)

x //= 10        #  x = x // 10   => x = 15
print(x % 10)

x //= 10        # x = 1
print(x % 10)