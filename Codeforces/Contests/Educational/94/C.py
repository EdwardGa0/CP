def solve():
    s = input()
    x = int(input())
    news = ['1'] * len(s)
    for i in range(len(s)):
        if s[i] == '0':
            if i+x < len(s):
                news[i+x] = '0'
            if i-x >= 0:
                news[i-x] = '0'
    for i in range(len(s)):
        if s[i] == '1':
            found = False
            if i+x < len(s) and news[i+x] == '1':
                found = True
            if i-x >= 0 and news[i-x] == '1':
                found = True
            if not found:
                return False
    return news

for _ in range(int(input())):
    res = solve()
    if res:
        print(''.join(res))
    else:
        print(-1)
