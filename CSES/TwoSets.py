n = int(input())
if n*(n+1)//2 & 1:
    print('NO')
else:
    print('YES')
    if n % 4 == 0:
        a = []
        for i in range(1, n//2, 2):
            a.append(i)
            a.append(n+1-i)
        print(len(a))
        print(*a)
        b = []
        for i in range(2, n//2+1, 2):
            b.append(i)
            b.append(n+1-i)
        print(len(b))
        print(*b)
    else:
        a = [1, 2]
        for i in range(4, (n-3)//2+3, 2):
            a.append(i)
            a.append(n+1-(i-3))
        print(len(a))
        print(*a)
        b = [3]
        for i in range(5, (n-3)//2+4, 2):
            b.append(i)
            b.append(n+1-(i-3))
        print(len(b))
        print(*b)