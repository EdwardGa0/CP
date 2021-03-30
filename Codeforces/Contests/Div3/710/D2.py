for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
    else:
        i1 = 0
        i2 = 1
        sofar = 0
        while i2 < n:
            if a[i1] != a[i2]:
                sofar += 2
                if i1+1 == i2:
                    i1 += 2
                    i2 += 2
                else:
                    i1 += 1
                    i2 += 1
            else:
                i2 += 1
        print(n-sofar)
    