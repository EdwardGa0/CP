for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cake = [0] * n
    for i, l in enumerate(a):
        if l > 0:
            if i-l+1 > 0:
                cake[i-l+1] += 1
            else:
                cake[0] += 1
            if i + 1 < n:
                cake[i+1] -= 1

    for i in range(1, n):
        cake[i] = cake[i-1] + cake[i]

    for i in range(n):
        if cake[i] > 1:
           cake[i] = 1 
    print(*cake)