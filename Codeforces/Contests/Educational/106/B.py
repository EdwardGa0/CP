def solve(s):
    idx = 0
    zeros = 0
    while idx < len(s):
        if s[idx] == '1':
            if idx > 0 and s[idx-1] == '1':
                break
        else:
            zeros += 1
        idx += 1
    while idx < len(s):
        if s[idx] == '0':
            if idx > 0 and s[idx-1] == '0':
                return False
        idx += 1
    return True

for _ in range(int(input())):
    s = input()
    
    if solve(s):
        print('YES')
    else:
        print('NO')
