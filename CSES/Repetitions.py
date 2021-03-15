s = input()
prev = ' '
ans = 1
rep = 1
for c in s:
    if c == prev:
        rep += 1
    else:
        prev = c
        ans = max(ans, rep)
        rep = 1
ans = max(ans, rep)
print(ans)