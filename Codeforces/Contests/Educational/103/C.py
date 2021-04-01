def read():
    return map(int, input().split())

for _ in range(int(input())):
    n = int(input())
    c = list(read())
    a = list(read())
    b = list(read())

    dp = [0] * n
    done = [False] * n
    for i in range(1, n):
        dp[i-1] = abs(a[i] - b[i])
    for i in range(n-1):
        for j in range(i+1, n):
            if not done[i]:
                if j != i+1:
                    dp[i] = max(dp[i], dp[i] + 2 + (c[j]-1) - abs(a[j]-b[j]))
                else:
                    dp[i] = max(dp[i], dp[i] + 2 + (c[j]-1))
            if j+1 == n or a[j+1] == b[j+1]:
                done[i] = True
    #print(dp)
    print(max(dp))