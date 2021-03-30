import sys, math
input = sys.stdin.buffer.readline

def solve(n, a):
    d = []
    for i in range(1, n):
        d.append(a[i]-a[i-1])
    m = 0
    for i in d:
        m = math.gcd(m, i-d[0])
    if m == 0:
        return [0]
    for i in a:
        if i >= m:
            return [-1]
    return [m, max(d)]
    
ans = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans.append(solve(n, a))
for i in ans:
    print(*i)
    