def ints():
    return map(int, input().split())

n, q = ints()
a = list(ints())
t = list(ints())

first = [-1] * 51
for i in range(n):
    if first[a[i]] < 0:
        first[a[i]] = i + 1

res = []
for i in range(q):
    res.append(first[t[i]])
    for j in range(len(first)):
        if first[j] < first[t[i]]:
            first[j] += 1
    first[t[i]] = 1
print(*res)