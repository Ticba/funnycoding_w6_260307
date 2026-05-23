"""4
+ string
+ apple
+ banana
- string"""

n = int(input())
L = []
for i in range(n):
    op, s = input().split()
    if op == '+':
        L.append(s)
    elif op == '-':
        L.remove(s)

print("\n".join(L))