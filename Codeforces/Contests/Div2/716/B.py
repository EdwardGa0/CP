mod = int(1e9) + 7

def pow(a, b):
    prod = 1
    for i in range(b):
        prod = (prod * a) % mod
    return prod

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(pow(n, k))