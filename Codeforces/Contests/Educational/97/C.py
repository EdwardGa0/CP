for _ in range(int(input())):
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    dp = [[0] * (2*n+1) for i in range(n+1)]
    min_dp = [0] * (2*n+1)
    for i in range(1, n+1):
        for T in range(i, 2*n+1):
            dp[i][T] = min(dp[i-1][i-1:T]) + abs(T - t[i-1])
    print(min(dp[n][n:]))