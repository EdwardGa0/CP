for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even = []
    odd = []
    for i in a:
        if i & 1:
            odd.append(i)
        else:
            even.append(i)
    print(*(even + odd))