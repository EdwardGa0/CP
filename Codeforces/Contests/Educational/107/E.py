n, m = map(int, input().split())
b = []
for i in range(n):
    temp = input()
    row = [False] * m
    for j in range(m):
        if temp[j] == 'o':
            row[j] = True
    b.append(row)

dp = [0] * (n*m)
def hori(b):
    t = 0
    for row in b:
        for i in range(m-1):
            if row[i] and row[i+1]:
                t += 1
                row[i] = False
                row[i+1] = False
                t += ways(b)
                row[i] = True
                row[i+1] = True