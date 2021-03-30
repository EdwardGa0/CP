for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ans = 0
    start = 0
    for i, c in enumerate(s):
        if c == '*':
            start = i
            ans += 1
            break
    
    while True:
        found = False
        for i in range(start+k, start, -1):
            if i >= n:
                continue
            if s[i] == '*':
                ans += 1
                start = i
                found = True
                break
        if not found:
            break

    print(ans)