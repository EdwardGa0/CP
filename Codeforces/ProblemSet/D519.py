from collections import defaultdict

val = list(map(int, input().split()))
s = input()

pos = [[] for i in range(26)]
sm = []
for i, c in enumerate(s):
    v = ord(c) - ord('a')
    if i == 0:
        sm.append(val[v])
    else:
        sm.append(sm[-1] + val[v])
    pos[v].append(i)

ans = 0
for c in range(26):
    m = defaultdict(int)
    for i in pos[c]:
        if i > 0:
            ans += m[sm[i-1]]
        m[sm[i]] += 1
print(ans)