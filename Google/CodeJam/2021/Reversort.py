for case in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cost = 0
    for i in range(n-1):
        j = a.index(min(a[i:]))
        cost += j-i+1
        a[i:j+1] = reversed(a[i:j+1])
    print('Case #{}:'.format(case+1), cost)