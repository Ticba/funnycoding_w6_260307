# 10 進制轉換成 2, 8, 16 進制
# 16 進制符號為 "0123456789ABCDEF"
# 請參考網站及上課影片
# https://runestone.academy/ns/books/published/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html

class Stack:
     def __init__(self):
         self.items = []        # list

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[-1]

     def size(self):
         return len(self.items)

def divideByBase(decNumber, base):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    ansString = ""
    while not remstack.isEmpty():
         ansString = ansString + digits[remstack.pop()]

    return ansString

print(divideByBase(180, 2))
