from collections import deque

def solve():
    n = int(input())
    s = input()
    ts = s.count('T')
    if ts != 2 * (n-ts):
        return False
    stack = 0
    for i in s:
        if i == 'T':
            stack += 1
        else:
            if stack == 0:
                return False
            stack -= 1
    stack = 0
    for i in reversed(s):
        if i == 'T':
            stack += 1
        else:
            if stack == 0:
                return False
            stack -= 1
    return True


for _ in range(int(input())):
    if solve():
        print('YES')
    else:
        print('NO')