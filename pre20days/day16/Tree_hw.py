# Tree 是什麼？

# Implement tree class

# BFS 怎麼做？
## 1. Code

## 2. 有沒有用到其他資料結構來處理 queue

# DFS 怎麼做？
## 1. Code

## 2. 有沒有用到其他資料結構來處理


class Node:
    pass

class Tree:
    def BFS():
        pass
    def DFS():
        pass


# What is a Tree?
# A tree is a hierarchical data structure made of nodes.
# The top node is called the root.
# A node can have child nodes.
# A node with no children is called a leaf.


# Implement a Tree class

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")

root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)


# BFS
# BFS means Breadth-First Search.
# It visits the tree one level at a time.
# BFS uses a queue, which follows FIFO:
# First In, First Out.

from collections import deque


def bfs(root):
    queue = deque([root])

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        for child in current.children:
            queue.append(child)


# DFS
# DFS means Depth-First Search.
# It goes as deep as possible before returning.
# Recursive DFS uses the call stack.
# A stack follows LIFO:
# Last In, First Out.

def dfs(node):

    for child in node.children:
        dfs(child)

    print(node.data, end=" ")   # postorder

print("BFS:")
bfs(root)

print("\nDFS:")
dfs(root)

# a
# | \
# b  c
# |\
# d e

# 輸出順序變成：d e b c a