n = int(input())
a = list(map(int, input().split()))
sa = sum(a)

def rec(i, s):
    if i == 0:
        return abs((sa-s) - s)
    return min(rec(i-1, s), rec(i-1, s+a[i]))

print(rec(n-1, 0))