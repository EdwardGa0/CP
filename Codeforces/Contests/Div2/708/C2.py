import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def solve(n):
    if n == 4:
        return ([1, 1, 2])
    if n & 1:
        return([1, (n-1)//2, (n-1)//2])
    else:
        if (n-2)//2 & 1:
            return([i*2 for i in solve(n//2)])
        else:
            return([2, (n-2)//2, (n-2)//2])

def rec(n, k):
    if k == 1:
        return [n]
    if k == 3:
        return solve(n)
    if n == k:
        return [1] * n
    if n & 1:
        return [1] + rec(n-1, k-1)
    if k & 1:
        return [2] + rec(n-2, k-1)
    return rec(n//2, k//2) + rec(n//2, k//2)
    

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(*rec(n, k))