for _ in range(int(input())):
    n = int(input())
    s = input()
    ones = 0
    for i in range(1, n):
        if s[i] == '1' and s[i-1] == '1':
            ones += 1
    zeros = 0
    for i in range(1, n):
        if s[i] == '0' and s[i-1] == '0':
            zeros += 1
    print(max(ones, zeros))