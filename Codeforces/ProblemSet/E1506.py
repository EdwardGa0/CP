import sys

input = sys.stdin.buffer.readline

def read():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    q = read()
    #minimum
    v = [False] * (n+1)
    it = 1
    pm = [0] * n
    for i in range(n):
        if i == 0 or q[i] != q[i-1]:
            v[q[i]] = True
            pm[i] = q[i]
        else:
            while v[it]:
                it += 1
            v[it] = True
            pm[i] = it
    print(*pm)
    #max
    nxt = [max(0, i-1) for i in range(0, n+1)]
    prv = [min(i+1, n) for i in range(0, n+1)]
    v = [False] * (n+1)
    pm = [0] * n
    for i in range(n):
        if i == 0 or q[i] != q[i-1]:
            pm[i] = q[i]
            it = nxt[q[i]]
        else:
            pm[i] = it
            it = nxt[it]
        nxt[prv[pm[i]]] = nxt[pm[i]]
        prv[nxt[pm[i]]] = prv[pm[i]]
    print(*pm)