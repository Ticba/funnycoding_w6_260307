# 物件導向程式設計
'''
1. 這個物件裡面有什麼資料
2. 這個物件有支援什麼功能
'''

class Fraction:
    def __init__(self, nu, de):     # method (class 自己才能用的 function)
        self.nu = nu
        self.de = de
    # __init__() -> 代表在定義 class 裡面的資料樣貌


    def __add__(self,otherfraction):
        newnu = self.nu*otherfraction.de + self.de*otherfraction.nu
        newde = self.de * otherfraction.de
        # 通分

        return Fraction(newnu,newde)

    def print_info(self):
        print(f"nu:{self.nu}, de:{self.de}")
  # f1 + f2


# 依照設計圖建立一個實體 -> 物件

f1 = Fraction(3, 5)     # 生成物件，並初始化
f1.print_info()

f2 = Fraction(2, 5)
f2.print_info()

(f1.__add__(f2)).print_info()
f3 = f1 + f2
f3.print_info()