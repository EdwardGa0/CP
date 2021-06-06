def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

ans = []
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if l[i] % 2 == 0 or l[j] % 2 == 0 or gcd(l[i], l[j]) > 1:
                s += 1
    
    ans.append(str(int(s)))
print('\n'.join(ans))

# odds = [i for i in l if i & 1]
#     even = n - len(odds)
#     s = (2*n-1-even) * (even / 2)
#     for i in range(even, n-1):
#         for j in range(i+1, n):
#             if gcd(l[i], l[j]) > 1:
#                 s += 1
