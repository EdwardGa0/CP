def toint(c):
    return ord(c) - ord('A')

def solve():
    n = int(input())
    s = input()
    visited = [False] * 26
    i = 0
    while i < n:
        if visited[toint(s[i])]:
            return False
        while i+1 < n and s[i+1] == s[i]:
            i += 1
        visited[toint(s[i])] = True
        i += 1
    return True

for _ in range(int(input())):
    if solve():
        print('YES')
    else:
        print('NO')