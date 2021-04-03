def solve():
    n = int(input())
    s = input()
    k = s.count('1')
    if s[0] != '1' or s[-1] != '1' or (n-k) & 1:
        return False
    a = []
    b = []
    ones = 0
    for i in range(n):
        if s[i] == '1':
            if ones < k//2:
                a.append('(')
                b.append('(')
            else:
                a.append(')')
                b.append(')')
            ones += 1
        else:
            if (i-ones) & 1:
                a.append('(')
                b.append(')')
            else:
                a.append(')')
                b.append('(')
    return (''.join(a), ''.join(b))

for _ in range(int(input())):
    res = solve()
    if res:
        print('YES')
        print(res[0])
        print(res[1])
    else:
        print('NO')