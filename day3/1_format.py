# 格式化
# English（舉例）
# 要求呈現的東西（文章）、字串
# 分段的時候要空兩格，且段落之間要換行。

'Hi, my name is ____, I am ____ years old.'

'''
Kevin 18
Alan  30
Mary   7

print('Hi, my name is Kevin, I am 18 years old.')
print('Hi, my name is Alan, I am 30 years old.')
print('Hi, my name is Mary, I am 7 years old.')
'''


# (1) "  %s  %d      "  % ('hello', 30)
'''
str1 = "  %s  %d      "  % ('hello', 30)
print(str1)

# %s -> 預留存放 str 的位置（以 string 輸出）
# %d -> 預留存放 int 的位置（以 int 輸出）

str2 = "%s%d" % ('030', True)
print(str2)
'''


'''
Kevin 18
Alan  30
Mary   7

print('Hi, my name is %s, I am %d years old.' % ('Kevin', 18))
print('Hi, my name is %s, I am %d years old.' % ('Alan', 30))
print('Hi, my name is %s, I am %d years old.' % ("Mary", 7))
'''


# (2) "{}{}".format('hello', 30)
# str1 = "{}{}".format('hello', True)
# print(str1)

# print('Hi, my name is {}, I am {} years old.'.format('Kevin', 18))
# print('Hi, my name is {}, I am {} years old.'.format('Alan', 30))
# print('Hi, my name is {}, I am {} years old.'.format("Mary", 7))


# (3) f-string    f'{'hello'}  {18}'
# print(f'{'hello'*2}lkj;asdfa{18*18}')

# print(f'Hi, my name is {'Kevin':____}, I am {18} years old.')
# print(f'Hi, my name is {'Alan'} , I am {30} years old.')
# print(f'Hi, my name is {'Mary'} , I am 0{7} years old.')




# {運算/資料:格式} 

print(f'Hi, my name is {'Kevin':>6s}, I am {18:02d} years old.')
print(f'Hi, my name is {'Alan':>6s}, I am {30:02d} years old.')
print(f'Hi, my name is {'Mary':>6s}, I am {7:02d} years old.')



# float 

print(f'{2/3:.2f}')