import sys, copy

input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

def ls(a, b):
    if a <= 1 or b <= 1:
        return 0
    return min(a-1, b//2-1) + min(b-1, a//2-1)

for t in range(int(input())):
    rows, cols = read()
    a = [[0] * (cols+2)]
    for i in range(rows):
        a.append([0] + list(read()) + [0])
    a.append([0] * (cols+2))

    a0 = copy.deepcopy(a)
    a1 = copy.deepcopy(a)
    a2 = copy.deepcopy(a)
    a3 = copy.deepcopy(a)

    for r in range(2, rows+1):
        for c in range(1, cols+1):
            if a0[r][c]:
                a0[r][c] += a0[r-1][c]
    
    for r in range(rows-1, 0, -1):
        for c in range(1, cols+1):
            if a1[r][c]:
                a1[r][c] += a1[r+1][c]
    
    for c in range(2, cols+1):
        for r in range(1, rows+1):
            if a2[r][c]:
                a2[r][c] += a2[r][c-1]
    
    for c in range(cols-1, 0, -1):
        for r in range(1, rows+1):
            if a3[r][c]:
                a3[r][c] += a3[r][c+1]

    res = 0
    for i in range(1, rows+1):
        for j in range(1, cols+1):
                v0 = a0[i][j]
                v1 = a1[i][j]
                h0 = a2[i][j]
                h1 = a3[i][j]
                temp = ls(v0, h0)+ls(v0, h1)+ls(v1, h0)+ls(v1, h1)
                res += temp
    print("Case #" + str(t+1) + ": " + str(res))