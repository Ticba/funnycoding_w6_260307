# counter 計數器

# 情境：要找 5 的倍數，輸出有幾個（個數）
'''
counter = 0
for i in range(1,101):
    if i % 5 == 0:
        counter += 1

print(counter)
'''

# 情境：要找 5 的倍數 | 但不能是 20 的倍數 | 且是 7 的倍數，輸出有幾個（個數）

counter = 0
for i in range(1,101):
    if i % 5 == 0 and i%20 != 0 and i%7 == 0:
        counter += 1

print(counter)