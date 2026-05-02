n = int(input())
dir = int(input())  # 0 left, 1 up, 2 right, 3 down

the_map = [list(map(int, input().split())) for _ in range(n)]

step = 2

dir_dict = {
    0: {'c':-1, 'r':0},
    1: {'c':0, 'r':-1},
    2: {'c':1, 'r':0},
    3: {'c':0, 'r':1},    
}

counter = 0
i = j = n // 2
while counter < n*n:
    for _ in range(step//2):
        print(the_map[i][j], end='')
        i, j = i + dir_dict[dir]['r'], j + dir_dict[dir]['c']
        counter += 1
        if counter >= n*n:
            break
    dir = (dir + 1) % 4
    step += 1
print()