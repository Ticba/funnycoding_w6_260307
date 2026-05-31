# 物件導向程式設計
'''
1. 這個物件裡面有什麼資料
2. 這個物件有支援什麼功能
'''

class Fraction:
    def __init__(self, nu, de):     # method (class 自己才能用的 function)
        self.nu = nu
        self.de = de
        self._simplify()
    # __init__() -> 代表在定義 class 裡面的資料樣貌

    def _gcd(self, m,n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n
    
    def _simplify(self):
        gcd = self._gcd(self.nu, self.de)
        self.nu //= gcd
        self.de //= gcd

    def __add__(self,otherfraction):
        newnu = self.nu*otherfraction.de + self.de*otherfraction.nu
        newde = self.de * otherfraction.de
        # 通分
        
        return Fraction(newnu,newde)        # create a new Fraction Object
    
    def __sub__(self, otherfraction):
        newnu = self.nu*otherfraction.de + self.de*otherfraction.nu
        newde = self.de * otherfraction.de
        # 通分
        
        return Fraction(newnu,newde)        # create a new Fraction Object
    
    def __mul__(self, otherfraction):
        pass

    def __truediv__(self, otherfraction):   # /
        pass

    # def __floordiv__(self, other):          # //
    #     pass

    def __eq__(self, otherfraction):        # equal
        return self.nu * otherfraction.de == self.de * otherfraction.nu

    def __gt__(self, otherfraction):        # greater than
        pass

    def __ge__(self, otherfraction):        # greater than or equal
        pass

    def __lt__(self, otherfraction):        # less than
        pass

    def __le__(self, otherfraction):        # less than or equal
        pass

    def __str__(self):
        pass

    def print_info(self):
        print(f"nu:{self.nu}, de:{self.de}")
  # f1 + f2


# 依照設計圖建立一個實體 -> 物件

f1 = Fraction(2, 5)     # 生成物件，並初始化
f1.print_info()

f2 = Fraction(2, 5)
f2.print_info()

(f1.__add__(f2)).print_info()
f3 = f1 + f2
f3.print_info()


print(f1 == f2)

# stack 放盤子（後放先拿 LIFO）
# queue 管子tube (FIFO)