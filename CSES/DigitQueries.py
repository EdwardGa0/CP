def f(n):
    t = 0
    exp = 0
    while True:
        add = (exp+1) * 9*pow(10, exp)
        if t+add < n:
            t += add
            exp += 1
        else:
            break
    return(int(str(pow(10, exp) + (n-t-1)//(exp+1))[(n-t)%(exp+1)-1]))

for _ in range(int(input())):
    print(f(int(input())))
    
# digits = 0
# for i in range(1, 1000):
#     for j in range(len(str(i))):
#         digits += 1
#         if int(str(i)[j]) != f(digits):
#             print(i)