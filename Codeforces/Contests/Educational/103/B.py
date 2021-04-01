import math

def read():
    return map(int, input().split())

for _ in range(int(input())):
    n, k = read()
    a = list(read())
    x = []
    for i in range(1, n):
        x.append(math.ceil(100*a[i]/k - sum(a[1:i])))
    print(max(0, max(x)-a[0]))