def ints():
    return map(int, input().split())

n = int(input())
a = list(ints())
b = list(ints())

def f(a, b):
    p = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            temp = b[j] * a[i-j]
            if not p[i]:
                p[i].append(temp)
            else:
                p[i].append(p[i][-1] + temp)
    pt = []
    for i in range(n):
        if not pt:
            pt.append(a[i]*b[i])
        else:
            pt.append(pt[-1] + a[i]*b[i])
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if j+i >= n:
                continue
            t = pt[-1] - pt[j]
            if i > 0:
                t += pt[i-1]
            t += p[j+i][j]
            if i > 0:
                t -= p[j+i][i-1]
            ans = max(ans, t)
    return max(ans, pt[-1])
            
print(max(f(a, b), f(list(reversed(a)), list(reversed(b)))))
