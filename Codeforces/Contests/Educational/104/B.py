def conv(k):
    return (k-1)%n+1

for _ in range(int(input())):
    n, k = map(int, input().split())
    if n & 1:
        print(conv((k-1)//(n//2)*(n//2+1) + (k-1)%(n//2)+1))
    else:
        print(conv(k))