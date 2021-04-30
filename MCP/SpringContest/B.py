from collections import deque

r, c, n, m = map(int, input().split())
r -= 1
c -= 1
a = []
for i in range(n):
    a.append(list(map(int, input())))

d = [[-1] * m for i in range(n)]
d[n-1][m-1] = 0

q = deque([(n-1, m-1)])
while q:
    i, j = q.popleft()
    if i == r and j == c:
        break
    for ip, jp in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
        if ip < 0 or ip >= n or jp < 0 or jp >= m:
            continue
        if a[ip][jp] == 1:
            continue
        q.append((ip, jp))
        a[ip][jp] = 1
        d[ip][jp] = d[i][j] + 1

print(d[r][c])
