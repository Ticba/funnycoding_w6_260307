# list 是什麼? 火車

L = [1, 2, 4]

# accessing (取用)

# 1. indexing
print(L[0])     # positive indexing
print(L[-1])    # negative indexing

# 2. slicing

print(L[0:2])


# change value (改變)

# 1. indexing
L[0] = 5        # L 的 0 項改成 5
print(L)

# 2. slicing
L[1:] = [100, 200]
print(L)


# Adding (新增)

# 1. .append()  加入到最後
# syntax list.append(資料)
L.append(300)
print(L)


# 2. .insert()  指定某一個位置加入
# syntax list.insert(index(位置), 資料)
L.insert(1,50)
print(L)


L.append(5)
# Remove (刪除)
# 1. .remove() 刪除指定的資料，如果有重複，刪除第一筆。
# syntax list.remove(資料內容)

L.remove(5)
print(L)


# 2. .pop() 刪除指定的位置
# syntax list.pop(index(位置))
L.pop(3)
print(L)


# sort 排序
L = [5, 3, 1, 2, 4, -20, 100, 30, 120]
L.sort()
print(L)

L[0]    # 最低
L[-1]   # 最高

print(f"最低:{L[0]}, 最高:{L[-1]}")