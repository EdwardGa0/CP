def solve():
    n = int(input())
    a = list(map(int, input().split()))
    t = 0
    for i in a:
        t ^= i
    if t == 0:
        return True
    if t not in a:
        return False
    a.remove(t)
    for i in a:
        t ^= i
        if t == 0:
            return True
    return False

for _ in range(int(input())):
    if solve():
        print('YES')
    else:
        print('NO')
