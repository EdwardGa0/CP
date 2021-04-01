import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    if n % k == 0:
        print(1)
    else:
        print(max(2, math.ceil(k/n)))