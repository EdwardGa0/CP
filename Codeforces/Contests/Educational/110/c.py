ans = []
for _ in range(int(input())):
    s = list(input())
    n = len(s)
    dp = [[0] * 2 for _ in range(n)]
    if s[0] == '0':
        dp[0][0] = 1
    elif s[0] == '1':
        dp[0][1] = 1
    else:
        dp[0] = [1, 1]
    for i in range(1, n):
        if s[i] == '0':
            dp[i][0] = dp[i-1][1] + 1
        elif s[i] == '1':
            dp[i][1] = dp[i-1][0] + 1
        else:
            dp[i][0] = dp[i-1][1] + 1
            dp[i][1] = dp[i-1][0] + 1
    ans.append(sum(max(i) for i in dp))
print('\n'.join(map(str, ans)))
