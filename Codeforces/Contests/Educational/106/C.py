import sys

def solve(n, costs):
    pref = [costs[0]]
    for i in costs[1:]:
        pref.append(i + pref[-1])

    
    i0 = 0
    i1 = 0
    min0 = costs[0]
    min1 = costs[1]
    m = n*(min0+min1)
    for i in range(2, n):
        if i & 1:
            i1 += 1
            min1 = min(min1, costs[i])
        else:
            i0 += 1
            min0 = min(min0, costs[i])
        newm = pref[i]-min0-min1 + (n-i0)*min0 + (n-i1)*min1
        m = min(m, newm)
    return m

for _ in range(int(input())):
    n = int(input())
    cost = list(map(int, input().split()))



    print(solve(n, cost))