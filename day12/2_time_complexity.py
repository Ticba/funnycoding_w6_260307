# 例子 1


n = int(input())        # O(1)
m = int(input())        # O(1)

count = 0               # O(1)

for _ in range(n):      # O(mxn)
    for _ in range(m):  # O(m)
        count += 100    # O(1)

# time complexity = O(mxn)


# 例子 2

n = int(input())
m = int(input())

count = 0

for _ in range(n):      
    for _ in range(m):  
        count += 100
        if count > 10000:
            break
    if count > 10000:
        break

# O(1) V
# O(n)
# O(mxn)