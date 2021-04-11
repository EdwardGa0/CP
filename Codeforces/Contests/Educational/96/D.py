import math

for _ in range(int(input())):
    n = int(input())
    s = input()
    pref = [1]
    for i in range(1, n):
        if s[i] == s[i-1]:
            pref[-1] += 1
        else:
            pref.append(1)
    q = list(reversed(pref))
    res = 0
    k = len(q) - 1
    while q:
        if q[-1] > 1:
            k -= 1
            q.pop()
            res += 1
        else:
            while k >= 0 and q[k] == 1:
                k -= 1
            if k >= 0:
                q[k] -= 1
                q.pop()
                res += 1
            else:
                res += math.ceil(len(q)/2)
                break
    print(res, flush=True)
