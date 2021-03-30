cases = int(input())
for case in range(cases):
    x, y, s = input().split()
    x = int(x)
    y = int(y)
    s = list(s)
    for i in range(len(s)):
        if s[i] == '?':
            if i > 0 and s[i-1] != '?':
                s[i] = s[i-1]
            elif i < len(s)-1 and s[i+1] != '?':
                s[i] = s[i+1]
    for i in reversed(range(len(s))):
        if s[i] == '?':
            if i > 0 and s[i-1] != '?':
                s[i] = s[i-1]
            elif i < len(s)-1 and s[i+1] != '?':
                s[i] = s[i+1]
    for i in range(len(s)):
        if s[i] == '?':
            if i > 0 and s[i-1] != '?':
                s[i] = s[i-1]
            elif i < len(s)-1 and s[i+1] != '?':
                s[i] = s[i+1]
    cost = 0
    if s[0] != '?':
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                if s[i] == 'J':
                    cost += x
                else:
                    cost += y
    print('Case #{}:'.format(case+1), cost)
            


