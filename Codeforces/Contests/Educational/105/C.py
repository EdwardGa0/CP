import sys
input = sys.stdin.buffer.readline

def read():
    return map(int, input().split())

for _ in range(int(input())):
    n, m = read()
    a = list(read())
    b = list(read())

    on = []
    start = 0
    for i in range(n):
        while start < n and b[start] < a[i]:
            start += 1
        if start < n:
            on.append(b[start] == a[i])
        else:
            on.append(False)
    on_sum = [sum(on)]
    for i in on:
        on_sum.append(on_sum[-1]-i)

    conseq = []
    start = 0
    for i in range(n+1):
        maxc = 0
        c = 0
        prev = b[start]
        if i < n:
            while start < n-1 and b[start] < a[i]:
                prev = b[start]
                start += 1
                if b[start] == prev:
                    c += 1
                else:
                    maxc = max(maxc, c)
                    c = 0
        else:
            while start < n-1:
                prev = b[start]
                start += 1
                if b[start] == prev:
                    c += 1
                else:
                    maxc = max(maxc, c)
                    c = 0
        conseq.append(c)

    print('len = ', len(conseq), len(on_sum))
    ans = 0
    for i in range(n+1):
        ans = max(ans, max(i, conseq[i]) + on_sum[i])
    print('ans = ', ans)
