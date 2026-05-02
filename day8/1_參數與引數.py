# Positional Arguments（位置對應）


def total(tens, ones):
    # 
    return tens * 10 + ones

print(total(5, 2)) # tens=5, ones=2
print(total(2, 5)) # tens=2, ones=5

# 結果不一樣是因為引數的位置不一樣


# Keyword Arguments（由關鍵字對應）

print(total(ones=5, tens=2))    # 25

# 混用

# print(total(5, 2, 3))



# 可變長度參數 *args -> arguments
def print_all(*args, t=3):   # 接收任意數量的位置引數
    print(args)

print_all(1, 2, 3, 4)   # 輸出 (1, 2, 3, 4)
print_all(1)            # 輸出 (1)
print_all(1,3,5, t=3)
'''
將所有位置引數打包成 tuple 傳給 args

'''


# 不可使用 sum()

def add_(*args):     # 將所有傳進來的數字加總，並且回傳
    pass
    return

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1,3,5)) #9
print(add(1,3,5,100)) 


# 可變長度的關鍵字對應參數

def info(**kwargs):     # kwargs -> keyword arguments
    print(kwargs)

info(name='Ticba', age=28)  # {'name': 'Ticba', 'age': 28}
'''
將所有關鍵字引數打包成 dict 傳給 kwargs

'''





print(1,2,3,4, sep='', end='\n\n')



def show(*args, **kwargs):
    print('Positional:', args)
    print('Keyword:', kwargs)

show(1, 2, name='Ticba', age=28)
