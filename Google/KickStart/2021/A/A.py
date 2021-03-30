for c in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    t = 0
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            t += 1
    print("Case #" + str(c+1) + ": " + str(abs(t-k)))