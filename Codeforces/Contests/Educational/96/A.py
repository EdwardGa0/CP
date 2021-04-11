for _ in range(int(input())):
    n = int(input())
    if n % 3 == 0:
        print(n//3, 0, 0)
    elif n >= 5 and (n-5) % 3 == 0:
        print((n-5)//3, 1, 0)
    elif n >= 7 and (n-7) % 3 == 0:
        print((n-7)//3, 0, 1)
    else:
        print(-1)