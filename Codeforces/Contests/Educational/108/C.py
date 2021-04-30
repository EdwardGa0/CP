def ints():
    return map(int, input().split())

for _ in range(int(input())):
    n = int(input())
    uni = list(ints())
    skill = list(ints())
    u = [[] for i in range(n)]
    for i in range(n):
        u[uni[i]-1].append(skill[i])
    for i in range(n):
        u[i].sort(reverse=True)
    p = [[0] for i in range(n)]
    for i in range(n):
        for j in u[i]:
            p[i].append(p[i][-1] + j)
    temp = []
    for i in p:
        if len(i) > 1:
            temp.append(i)
    p = temp

    ans = []
    for i in range(1, n+1):
        a = 0
        if not(ans and ans[-1] == 0):
            for j in p:
                k = len(j) - 1
                a += j[k-(k%i)]
        ans.append(a)
    print(*ans)