import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

for _ in range(int(input())):
    s1 = input()
    s2 = input()
    l = lcm(len(s1), len(s2))
    if s1 * (l // len(s1)) == s2 * (l // len(s2)):
        print(s1 * (l // len(s1)))
    else:
        print(-1)