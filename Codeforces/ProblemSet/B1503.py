n = int(input())
b = [[0] * (n+1) for i in range(n+1)]

def fill(nc):
    p = [i for i in [1, 2, 3] if i != nc]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not b[i][j]:
                for c in p:
                    if b[i-1][j] != c and b[i][j-1] != c:
                        b[i][j] = c
                        return (c, i, j)

for i in range(n**2):
    c = int(input())
    res = fill(c)
    if res:
        print(*res, flush=True)