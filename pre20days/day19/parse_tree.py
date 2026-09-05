# 練習：建立運算樹


# 輸入：有括號的運算式
# ((3+5)*(6-3))
# (2-1)



# *
# | \
# +   -
# |\  |\ 
# 3 5 6 3


# -
# | \
# 2  1


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value)



sInput = "((3+5)*(6-3))"
root = Node()
current = root

for s in sInput:
    if s == '(':
        current.left = Node()
        current.left.parent = current
        current = current.left
    elif s in '0123456789':
        current.value = int(s)
        current = current.parent

    elif s == ')':
        current = current.parent
    else: # operator
        current.value = s
        current.right = Node()
        current.right.parent = current
        current = current.right


current = root
print(current)
print(current.left)
print(current.right)
current = current.left
print(current.left)
print(current.right)
current = current.parent.right
print(current.left)
print(current.right)




# root.left = Node("+")
# root.right = Node("-")

# root.left.left = Node("3")
# root.left.right = Node("5")

# root.right.left = Node("6")
# root.right.right = Node("3")


# print(root.value)
# print(root.left.value, root.right.value)
# print(root.left.left.value, root.left.right.value,
#       root.right.left.value, root.right.right.value)


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        return self.left is None and self.right is None


def build_tree(expression):
    root = Node()
    current = root
    number = ""

    for s in expression:

        if s.isdigit():
            number += s
            continue

        if number != "":
            current.value = int(number)
            number = ""
            current = current.parent

        if s == '(':
            current.left = Node()
            current.left.parent = current
            current = current.left

        elif s == ')':
            current = current.parent

        elif s in "+-*/":
            current.value = s

            current.right = Node()
            current.right.parent = current
            current = current.right

    if number != "":
        current.value = int(number)

    return root


def evaluate(node):

    if node.is_leaf():
        return node.value

    left_value = evaluate(node.left)
    right_value = evaluate(node.right)

    if node.value == '+':
        return left_value + right_value

    elif node.value == '-':
        return left_value - right_value

    elif node.value == '*':
        return left_value * right_value

    elif node.value == '/':
        return left_value / right_value


def inorder(node):

    if node is not None:
        inorder(node.left)

        print(node.value, end=" ")

        inorder(node.right)


def preorder(node):

    if node is not None:
        print(node.value, end=" ")

        preorder(node.left)
        preorder(node.right)


def postorder(node):

    if node is not None:
        postorder(node.left)
        postorder(node.right)

        print(node.value, end=" ")


def print_tree(node, level=0, side="Root"):

    if node is not None:

        print_tree(node.right, level + 1, "R")

        print("    " * level + side + ": " + str(node.value))

        print_tree(node.left, level + 1, "L")


sInput = "((3+5)*(6-3))"

root = build_tree(sInput)


print("TREE:")
print_tree(root)


print("\nInorder:")
inorder(root)

print("\n\nPreorder:")
preorder(root)

print("\n\nPostorder:")
postorder(root)


print("\n\nAnswer:")
print(evaluate(root))