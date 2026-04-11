'''
input: 3


output:
__*
_**
***
'''
# 看成要輸出兩個符號，先輸出 "_" 再輸出 "*"
# _ 的個數 從 2(3-1) -> 1(前一行的減 1) -> 0
# * 的個數 從 1 -> 2 -> 3



'''
input: 5

output:
____*
___**
__***
_****
*****
'''


# 看成要輸出兩個符號，先輸出 "_" 再輸出 "*"
# _ 的個數 從 4(5-1) -> 3 -> 2 -> 1 -> 0
# * 的個數 從 1 -> 2 -> 3 -> 4 -> 5


n = int(input())

num_under_line = n
num_star = 0

for i in range(0, n):
    num_under_line -= 1
    num_star += 1
    print('_' * num_under_line + '*' * num_star)
    # 1: num_under_line = 2, num_star = 1
    # 2: num_under_line = 1, num_star = 2

    # recursive 遞迴


# 你的寫法
n = int(input())

for i in range(1, n + 1):           # i = 1, 2,... , n
    print("_" * (n - i) + "*" * i)  # * = (n-i)





# 數學

'''
an = 1, 2, 3, 4, 5, ....

表示法：
一般式 (general form)
an = n
a1 = 1
a2 = 2

recursive
a_n = a_n-1 + 1
後 = 前 + 1
a_1 = 1

a_2 = 2
a_3 = 3


ai = (5-i)
a1 = 4
a2 = 3
a3 = 2



'''