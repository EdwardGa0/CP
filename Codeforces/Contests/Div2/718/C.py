n = int(input())
perm = list(map(int, input().split()))
grid = [[0] * n for i in range(n)]
for i in range(n):
    r = i
    c = i
    for j in range(perm[i]):
        grid[r][c] = perm[i]
        if c == 0 or grid[r][c-1]:
            r += 1
        else:
            c -= 1
        
for i, row in enumerate(grid):
    print(*row[:i+1])