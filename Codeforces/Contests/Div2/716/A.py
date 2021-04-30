import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if math.isqrt(i)**2 != i:
            return True
    return False

for _ in range(int(input())):
    if solve():
        print('YES')
    else:
        print('NO')