def read():
    return map(int, input().split())

for _ in range(int(input())):
    n, k = read()
    a = list(read())
    a.sort(reverse=True)
    print(sum(a[:k+1]))