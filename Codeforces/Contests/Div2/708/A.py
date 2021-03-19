for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    first = sorted(list(set(a)))

    for i in first:
        a.remove(i)
    
    print(*(first+a))