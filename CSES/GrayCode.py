n = int(input())
ans = [["0"], ["1"]]
for i in range(n-1):
    ans.extend([i.copy() for i in reversed(ans)])
    for j, s in enumerate(ans):
        if j < len(ans)//2:
            s.append("0")
        else:
            s.append("1")
for i in ans:
    print(''.join(i))