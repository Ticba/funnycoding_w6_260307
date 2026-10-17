class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i): # 在 insert() 中使用
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i): # 在 delMin() 中使用
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self,i):   # 在 percDown() 中使用
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def __str__(self):
        s = ''
        for data in self.heapList:
            s += ',' + str(data)
        return s[3:]

bh = BinHeap()

bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh)   # [3, 7, 5, 11]

for i in range(4):
    ret = bh.delMin()
    print(ret, '|', bh)

# 3
# 7 5
# |
# 11


# binary_heap 的應用