# children List

# 用 node 表示樹



# 1
# | \
# 2  3
# 用 list 表示樹

# list 的集合（不是數學的集合）
# 集合：dict

# online judge 常需要
nodes = {
    1: [2, 3],
    2: [],
    3: []
}

# 實際做 project 比較會用
values = {
    1: {'name':'Leo', 'age':20}

}




# 題目可能會怎麼給（n, m) n 是父母節點, m 是子節點
5
1,2
1,3
2,4
2,5
3,6

# 1
# 2  3
# | \  \ 
# 4  5   6


'''tree = {}
for i in range(int(input())):
    a, b = input().split()
    if a not in tree:
        tree[a] = []
    tree[a].append(b)

print(tree)'''

# {'1': ['2', '3'], '2': ['4', '5'], '3': ['6']}


# dfs
1 - 2 - 4 - 5 - 3 - 6
def dfs(node, parent):
    print(node)

    if node in tree:
        for next in tree[node]:
            dfs(next, node)

# dfs('1', None)

# edgeList

{'1': ['2', '3'], '2': ['1', '4', '5'], '3': ['1', '6'], '4':['2'], '5':['2'], '6':['3']}
# 挑戰：修改上面的 tree 程式，改成可以將輸入存成 edgeList 的程式

tree = {}
for i in range(int(input())):
    a, b = input().split()
    if a not in tree:
        tree[a] = []
    tree[a].append(b)

    if b not in tree:
        tree[b] = []
    tree[b].append(a)

print(tree)

def dfs(node, parent):
    print(node)

    if node in tree:
        for next_node in tree[node]:    # nxt
            if next_node != parent:
                dfs(next_node, node)

dfs('1', None)
print(tree)




# zerojudge b517, b518


# b517 

# 要如何用 dfs 來判斷一個 graph 是不是 tree
# 修改成在走節點的過程中，

'''
你可能會需要用到 set()
1. 檢查有沒有 cycle

2. 檢查是不是多個 part

'''


# 修改 dfs 來完成
'''
(1) 計算 depth of nodes

(2) 計算 height of a tree

(3) 計算 size of a tree

(4) 計算 distance of two nodes

(5) 計算 tree diameter

'''

