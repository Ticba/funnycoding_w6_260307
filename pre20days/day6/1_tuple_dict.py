# 不能改動的 list

# syntax this_is_a_tuple = ()

this_is_a_tuple = (3, 4)
print(this_is_a_tuple)

# test

# write 寫(X)
# this_is_a_tuple[0] = 5

# read 讀(O)
print(this_is_a_tuple[0])


s = "a b c"
(x,y,z) = s.split()



# dict

# 成對(配對)

# 例一
# key:value
# key 不能重複，value 沒有限制
# 1:滷肉飯
# 2:肉燥麵
# 4:陽春麵

# 例二
# 圖書館 ISBN
# 編號讓工作人員方便將出快速整理回原位
# A 區、B 區...
# A1 、 A2...


# A12234: 小王子
# B23344: 英文字典


# syntax this_is_a_dict = {key:value}

A_dict = {1:"滷肉飯", 2:'肉燥麵', 4:'陽春麵'}
B_dict = {'Tony': 90, 'Mary':90, 'Leo':99}

# print(A_dict[3])
print(B_dict['Leo'])   # 查 key 對應的 value