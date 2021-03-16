def solve(a, b):
    if abs(a-b) > min(a, b):
        return False
    return (a+b)%3 == 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    if solve(a, b):
        print("YES")
    else:
        print("NO")