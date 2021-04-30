for _ in range(int(input())):
    a, b, c = map(int, input().split())
    C = 10**(c-1)
    A = C
    B = C
    while len(str(A)) < a:
        A *= 2
    while len(str(B)) < b:
        B *= 3
    print(A, B)