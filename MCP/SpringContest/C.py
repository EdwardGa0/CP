n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            a[i][j] = min(a[i][j], a[i][k] + a[k][j])

print(sum(map(sum, a)))