import math

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r


for _ in range(int(input())):
    n = int(input())
    while math.gcd(n, sum_digits(n)) <= 1:
        n += 1
    print(n)
