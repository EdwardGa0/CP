def solve():
    s = input()
    return s.count('?') % 2 == 0 and not s[0] == ')' and not s[-1] == '('

for _ in range(int(input())):
    if solve():
        print('YES')
    else:
        print('NO')