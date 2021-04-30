n = int(input())
a = list(map(int, input().split()))
a.sort()
dp = [[0] * n for i in range(n)]

for l in range(n-2, -1, -1):
    for r in range(l, n):
        dp[l][r] = a[r] - a[l] + min(dp[l+1][r], dp[l][r-1])

print(dp[0][n-1])