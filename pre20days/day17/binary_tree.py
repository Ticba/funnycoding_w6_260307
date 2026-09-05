# 每個節點（node）只能有左右 child



class TreeNode:
    def __init__(self, data):
        self.data = data
        self.rightchild = None
        self.leftchild = None

    def add_right_child(self, child):
        if self.rightchild:
            child.rightchild = self.rightchild
        self.rightchild = child

    def add_left_child(self, child):
        if self.leftchild:
            child.leftchild = self.leftchild
        self.leftchild = child


#   a
#   | \
#   b  c

# insert d to a 的左邊

#   a
#   | \
#   d  c
#   |\
#   b None

root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")


root.add_left_child(node_b)
root.add_right_child(node_c)
root.add_left_child(node_d)

from collections import deque

def bfs(root):
    queue = deque([root])

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.leftchild:
            queue.append(current.leftchild)
        if current.rightchild:
            queue.append(current.rightchild)


bfs(root)