# 分支（根據不同狀況）
# if-elif-else

# match-case


grade = 'C' # or 'B' or 'C' or 'D' or 'F'

'''
match 變數名稱/運算:
    case case1_value:
        case1 block
    case case2_value:
        case2 block

'''

match grade:
    case 'A':
        print("A")
    case 'B':
        print("B")
    case _: # 外卡
        print("others")