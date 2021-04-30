# from functools import cache

n = 0
mod = int(1e9) + 7

#@cache
def solve(k, p, right):
    res = 1
    if k > 1:
        if right:
            for i in range(p+1, n+1):
                res = (res + solve(k-1, i, False)) % mod
        else:
            for i in range(p-1, 0, -1):
                res = (res + solve(k-1, i, True)) % mod
    return res

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(solve(k, 0, True))
    #solve.cache_clear()