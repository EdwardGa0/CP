import math

def solve(a, b):
    ap = 0
    bp = 0
    a -= 1
    turn = 0
    if a >= b:
        ap += a - b + 1
        a = b
        turn = 1
    else:
        bp += b - a
        b = a
    if turn:
        bp += math.ceil(b/2)
        ap += a//2
    else:
        bp += b//2
        ap += math.ceil(a/2)
    return ap, bp

# for i in range(1, 20):
#     for j in range(1, 20):
#         a, b = solve(i, j)
#         if a != i-1 or b != j:
#             print(i, j)

print(solve(3, 2))