# list comprehension

a = []
for i in range(10000):
    if i%3 == 0:
        a.append(i+1)


b = [i+1 for i in range(10000) if (i+1)%3 == 0]
# syntax [expression for ___ in range()]

print(b)


nine_nine = []      # '1x1=1'
for i in range(1, 10):
    for j in range(1, 10):
        nine_nine.append(f'{i}x{j}={i*j}')

nine_nine_2 = [f'{i}x{j}={i*j}' for i in range(1,10) for j in range(1, 10)]

print(nine_nine_2)







# tuple comprehension

nine_nine_tuple = (f'{i}x{j}={i*j}' for i in range(1,10) for j in range(1, 10))
print(list(nine_nine_tuple))


# 100 個 0

zero_list = [0 for i in range(100)]
print(zero_list)