import sys
input = sys.stdin.readline

def read():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = read()
    for i in range(n):
        a[i] = (a[i] + i) % n
    if len(set(a)) == n:
        print('YES')
    else:
        print('NO')