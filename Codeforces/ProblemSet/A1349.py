import math

n = int(input())
a = list(map(int, input().split()))
res = a[0]
for i in a[1:]:
    res = math.gcd(res, i)
print(res)