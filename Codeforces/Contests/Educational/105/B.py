def solve():
    n, u, r, d, l = map(int, input().split())
    ring = [u, r, d, l]
    for i in range(16):
        b = bin(i)[2:].zfill(4)
        for j in range(4):
            s = int(b[j]) + int(b[(j+1)%4])
            if s > ring[j] or n-(2-s) < ring[j]:
                break
        else:
            return True
    return False

for _ in range(int(input())):
    if solve():
        print('YES')
    else:
        print('NO')