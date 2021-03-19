import sys

input = sys.stdin.readline

def read():
    return map(int, input().split())

for _ in range(int(input())):
    n, m = read()
    a = list(read())
    md = [0] * int(1e5)
    for i in a:
        md[i%m] += 1

    s = 0
    if md[0]:
        s += 1
    for i in range(1, m//2+1):
        if not (md[i] == 0 and md[m-i] == 0):
            s += max(abs(md[i] - md[m-i]), 1)

    # print('mod')
    # for i in range(m):
        
    #     print(md[i], end=' ')
    
    print(s)
