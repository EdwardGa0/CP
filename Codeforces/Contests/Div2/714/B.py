mod = int(1e9 + 7)

def mult(a, b):
    return (a % mod) * (b % mod)

def fact(l, r):
    res = 1
    if l <= r:
        for i in range(l, r+1):
            res = mult(res, i)
    return res

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if all(a[0] == i for i in a):
        print(fact(1, n), flush=True)
    else:
        zeros = a.count(0)
        print(mult(fact(zeros-1, zeros), fact(1, n-2)))
