for _ in range(int(input())):
    n = int(input())
    if n < 0:
        print(-n)
    else:
        s = 0
        i = 0
        while s < n:
            i += 1
            s += i
        if s == n or s - n > 1:
            print(i)
        else:
            print(i+1)
