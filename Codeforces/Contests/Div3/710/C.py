import sys

def solve():
    a = input()
    b = input()
    if len(b) < len(a):
        a, b = b, a
    ans = len(a) + len(b)
    for i in range(0, len(a)):
        for j in range(i+1, len(a)+1):
            if a[i:j] in b:
                ans = min(ans, len(a) + len(b) - 2*(j-i))
    return ans

for _ in range(int(input())):
    print(solve())

    
                