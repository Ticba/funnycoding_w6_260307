# variable

# 以功能來分別
# 1. 拿來存數字 int, float
a = 3   # int 整數
b = 3.0 # float 浮點數

"""
運算子  1 + 1  -> 1 就是運算元 operand,  + 就是運算子 operator
math

program(python)
+ add(加), - minus(減), * times(乘), / divide(小數除法), // Q(取商數), % Remainder(取餘數), ** power(次方)

"""
print(2+3, 2-3, 2*3, 2/3, 2//3, 2%3, 2**3)    # 5 -1 6 0.6666 0 2 8

# 2. 拿來存判斷的結果 bool (True/False)
c = True
d = False
e = (3 > 0)     # True

"""
運算子 and, or, not
True and True (2>0 and 2<5)-> True

運動會 如果
1. 大家跑步第一名    -> True
2. 秩序良好         -> True

那麼老師請大家喝飲料
(1.有發生 and 2.有發生) -> True
"""

# 3. 拿來存字 str
f = "aksdj;falksjdf;"
g = "13"

"""
運算子 + (串接字), *(重複字)
"""
s1 = '123'
s2 = '123'
print(s1+s2)    # '123' + '123' => '123123'
# str + str => 串接


s3 = '123'
i4 = 3
print(s3 * i4)  # '123' * 3 => '123123123'
# str * int


# 挑戰題：預測結果
s5 = 'str'
s6 = '3'
i7 = 4
i8 = 2
print((s5 * i8) + (s6 * i7), 'apple')        # 結果？ strstr3333
# print 顯示了幾個東西？ 1 個



# variable 規則/禁止事項

# 命名規則
"""
1 只能由大小寫英文字母、數字、_、中文組成變數的名稱
2 變數名稱的第一個字不能是數字
"""

# 命名禁止事項
"""
變數名稱不能是 保留字
例如：
input
print
if
else
"""

_aaa = 5