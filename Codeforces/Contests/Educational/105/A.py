from collections import deque

def solve(s):
    a = []
    a.extend(transform(s, 'A'))
    a.extend(transform(s, 'B'))
    a.extend(transform(s, 'C'))
    return any(map(is_stack, a))

def transform(s, t):
    res0 = []
    res1 = []
    for i in s:
        if i == t:
            res0.append('(')
            res1.append(')')
        else:
            res0.append(')')
            res1.append('(')
    return [res0, res1]

def is_stack(s):
    d = []
    for i in s:
        if i == '(':
            d.append('(')
        else:
            if not d:
                return False
            if d.pop() != '(':
                return False
    return not d


for _ in range(int(input())):
    if solve(input()):
        print('YES')
    else:
        print('NO')
