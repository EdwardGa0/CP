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

# for i in range(3, 1000):
#     res = solve(i)
#     if sum(res) != i:
#         print(i, res)
#     try:
#         if lcm(lcm(res[0], res[1]), res[2]) > i/2:
#             print(i, res)
#     except:
#         print(i, res)

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(*solve(n))
    