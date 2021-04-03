for _ in range(int(input())):
    s = input()
    for i in range(len(s)):
        if s[len(s) - i - 1] != 'a':
            print('YES')
            print(s[:i] + 'a' + s[i:])
            break
    else:
        print('NO')