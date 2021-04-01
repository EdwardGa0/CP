for _ in range(int(input())):
    n = int(input())
    if n & 1:
        maxw = (n-1)//2
        wins = [0] * n
        res = []
        for i in range(n-1):
            for j in range(i+1, n):
                if wins[i] < maxw:
                    res.append(1)
                    wins[i] += 1
                else:
                    res.append(-1)
                    wins[j] += 1
        print(*res)
    else:
        m = 12
        o = 15
        points = [0] * n
        res = []
        for i in range(n-1):
            for j in range(i+1, n):
                if points[i] + 3 <= m:
                    res.append(1)
                    points[i] += 3
                elif points[i] + 1 <= o:
                    res.append(0)
                    points[i] += 1
                    points[j] += 1
                else:
                    res.append(-1)
                    points[j] += 3
        print(m)
        print(*res)
        print(points)
        