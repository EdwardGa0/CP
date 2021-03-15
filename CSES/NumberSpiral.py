import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    y, x = map(int, input().split())
    m = max(y, x)
    corner = m*(m-1)+1
    if m & 1: #right
        corner -= y-x
    else:
        corner += y-x
    print(corner)