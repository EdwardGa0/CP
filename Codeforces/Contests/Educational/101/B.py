def read():
    return list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = read()
    m = int(input())
    b = read()
    pa = [0]
    for i in a:
        pa.append(pa[-1] + i)
    pb = [0]
    for i in b:
        pb.append(pb[-1] + i)
    print(max(pa) + max(pb))