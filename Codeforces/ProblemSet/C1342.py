import sys, math
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

def solve(x, b, lcm):
    d, r = divmod(x, lcm)
    return d*(lcm-b) + max(0, r-b+1)

for _ in range(int(input())):
    a, b, q = read()
    if a > b:
        a, b = b, a
    g = math.gcd(a, b)
    lcm = a*b//g
    ans = []
    for i in range(q):
        l, r = read()
        ans.append(solve(r, b, lcm) - solve(l-1, b, lcm))
    print(*ans)