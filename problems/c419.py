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


