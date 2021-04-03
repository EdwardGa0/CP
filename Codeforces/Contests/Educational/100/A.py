def solve():
    a, b, c = map(int, input().split())
    if (a + b + c) % 9 != 0:
        return False
    return min(a, b, c) >= (a + b + c) // 9

for _ in range(int(input())):
    if solve():
        print('YES')
    else:
        print('NO')