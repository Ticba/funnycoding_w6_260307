import sys
# sys.stdin = open('day20/zerojudge/b517.in')

n = int(input())

tree = {}

visited = set()

def dfs(node, parent):
    if not parent:
        visited.clear()

    visited.add(node)

    for next_node in tree[node]:
        if next_node == parent:
            continue

        if next_node in visited:
            return False   # 發現 cycle

        if not dfs(next_node, node):
            return False
    if not parent and len(visited) != len(tree):
        return False
    return True

for _ in range(n):
    
    root = None
# bulid tree
    input_str = input().split()
    for s in input_str:
        i, j = s.split(',')
        if not root:
            root = i
        if i in tree:
            tree[i].append(j)
        else:
            tree[i] = [j]

        if j in tree:
            tree[j].append(i)
        else:
            tree[j] = [i]
# check
    if dfs(root, None):
        print('T')
    else:
        print('F')
# clear
    tree = {}


        

