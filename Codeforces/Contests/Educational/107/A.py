import sys
input = sys.stdin.buffer.readline

for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    res = 0
    for i in r:
        if i == 1 or i == 3:
            res += 1
    print(res)