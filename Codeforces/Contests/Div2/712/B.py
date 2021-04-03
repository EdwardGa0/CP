def bit_not(n):
    return bin((1 << len(n)) - 1 - int(n, 2))[2:].zfill(len(n))

def solve():
    n = int(input())
    a = input()
    b = input()
    if a == b:
        return True
    if a.count('0') != b.count('0'):
        return False
    l = 0
    az = a[:2].count('0')
    bz = b[:2].count('0')
    for i in range(2, n+1):
        if not (i & 1):
            if az == i//2 and bz == i//2:
                if not (a[l:i] == b[l:i] or bit_not(a[l:i]) == b[l:i]):
                    return False
                l = i
        if i < n:
            if a[i] == '0':
                az += 1
            if b[i] == '0':
                bz += 1
    return a[l:] == b[l:]
    

for _ in range(int(input())):
    if solve():
        print('YES')
    else:
        print('NO')
