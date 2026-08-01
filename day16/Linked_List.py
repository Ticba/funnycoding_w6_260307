class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def setNext(self, other):
        self.next = other

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def __str__(self):
        return f"({self.data})"

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def find_node(self):
        pass
        # 回傳對應的 Node

    def __str__(self):
        self.current = self.head
        ret_s = str(self.head)
        self.current = self.current.next

        while self.current != None:
            ret_s += "->" + str(self.current)
            self.current = self.current.next
        return ret_s

LL = LinkedList()
LL.head = Node(10)
LL.current = LL.head

for i in range(1, 10):
    LL.current.setNext(Node((i+1)*10))
    LL.current = LL.current.next

print(LL)

# 練習
# 製造十個 node，第 n 個 Node 他的 next 是第 n+1 個 Node
# data 就自行設定（十個 Node Data 不重複）






# 練習
# 內容
"建立一個 LL ，每一個 Node 需要按照給定的順序添加到 LL"

# 輸入說明：
# 每行給定 id data after 代表 Node 編號 儲存的資料 皆在哪一個 Node 後面

# 輸出說明：
# 按照格式將完整 LL print 出結果

# input:
# 1 a None
# 2 b 1
# 3 f 1

# output:
# (a) -> (f) -> (b)