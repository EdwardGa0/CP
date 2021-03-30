import sys, math

input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

for _ in range(int(input())):
    n, w = read()
    l = list(read())
    print(math.ceil(sum(l)/w))