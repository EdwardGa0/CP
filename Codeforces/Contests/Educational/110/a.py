ans = []
for _ in range(int(input())):
    l = list(map(int, input().split()))
    L = sorted(l)
    if (max(l[0], l[1]) in L[2:] and max(l[2], l[3]) in L[2:]):
        ans.append('YES')
    else:
        ans.append('NO')
print('\n'.join(ans))