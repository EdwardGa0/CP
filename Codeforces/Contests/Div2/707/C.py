n = int(input())
a = list(map(int, input().split()))
a.sort()
sums = set()

def solve(l, r):
    if a[l]+a[r] in sums:
        return True
    sums.add(a[l]+a[r])
    ans = []
    if r-l > 0:
        return solve(l+1, r) or solve(l, r-1)
    return False

#not finished