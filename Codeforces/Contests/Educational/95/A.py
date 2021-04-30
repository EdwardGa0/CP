import math

for _ in range(int(input())):
    x, y, k = map(int, input().split())
    sticks = k + y*k
    if (sticks-1) % (x-1) == 0:
        print((sticks-1)//(x-1) + k)
    else:
        print((sticks-1)//(x-1) + 1 + k)