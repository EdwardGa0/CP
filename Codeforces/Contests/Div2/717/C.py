n = int(input())
a = list(map(int, input().split()))

def rec(s, i, d):
    if s == 0:
        return d
    if i == n:
        return -1
    if 
    nodel = rec(s, i+1, d) or rec(s + a[i], i+1, d)
    if nodel >= 0:
        return nodel
    if a[i] % 2 == 0:
        delete = rec(s - a[i]//2, i+1, d+1)
    return delete

