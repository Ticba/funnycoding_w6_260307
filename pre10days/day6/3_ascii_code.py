# ascii code
'''
chr(編號)->字元 ：將編號轉換成字元

ord(字元)->編號 ：將字元轉換成編號
'''

print(chr(65))
print(ord('a'))



# 兩個英文字母中間差幾格
甲 = 'A'
乙 = 'K'

print(abs(ord(甲)-ord(乙)))



# 加密：
# A(65) -> D
# B -> E
# Z(90) -> C(67)
# Y(89) -> B
# X(88) -> A
# W(87)

"""90 - 65 = 25
25 + 3 = 28
28 % 26 = 2
65 + 2 = 67
chr(67) # 'Z'"""


s = 'zoo' # 'a', 'p', 'p', 'l', 'e'
for c in s:
    if ord(c) > 87:
        print(chr(ord(c)-23), end='')
    else:
        print(chr(ord(c)+3), end='')
print()



# 解密：
# D -> A
# E -> B
# C -> Z




# A B C D E (25)