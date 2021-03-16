def rec(n, source, destination, temp):
    if n == 1:
        print(source, destination)
        return
    rec(n-1, source, temp, destination)
    print(source, destination)
    rec(n-1, temp, destination, source)

n = int(input())
print(pow(2, n)-1)
rec(n, 1, 3, 2)