n = int(input())
for i in range(1, n+1):
    a = i*i
    b = a*(a-1)//2
    c = 4*(i-1)*(i-2)
    print(b-c)