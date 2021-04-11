import math, sys

input = sys.stdin.buffer.readline

def read():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = read()
    suma = sum(a)
    s = max(max(a), math.ceil(suma/(n-1)))
    print(s*(n-1) - suma)