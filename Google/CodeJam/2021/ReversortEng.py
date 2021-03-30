import itertools

d = {}

def get_min(l):
    if l not in d:
        d[l] = l.index(min(l))
    return d[l]


for case in range(int(input())):
    n, c = map(int, input().split())
    a = list(range(1, n+1))
    for L in map(list, itertools.permutations(a)):
        l = L.copy()
        cost = 0
        for i in range(n-1):
            j = i + get_min(tuple(l[i:]))
            cost += j-i+1
            l[i:j+1] = reversed(l[i:j+1])
        if cost == c:
            print('Case #{}:'.format(case+1), *L)
            break
    else:
        print('Case #{}:'.format(case+1), 'IMPOSSIBLE')