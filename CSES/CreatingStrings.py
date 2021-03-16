s = input()

def rec(s):
    ans = []
    if len(s) == 1:
        return [s]
    for i in set(s):
        ans.extend([i+j for j in rec(s.replace(i, "", 1))])
    return ans

ans = rec(s)
ans.sort()
print(len(ans))
print(*ans)