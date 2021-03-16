from itertools import permutations

board = []
for i in range(8):
    s = input()
    temp = [True] * 8
    for j, c in enumerate(s):
        if c == '*':
            temp[j] = False
    board.append(temp)

perms = permutations(list(range(8)))

def valid_perm(p):
    for i, j in enumerate(p):
        if not board[i][j]:
            return False
    t = [False] * 15
    for i, j in enumerate(p):
        if t[j-i]:
            return False
        t[j-i] = True
    t = [False] * 15
    for i, j in enumerate(p):
        if t[j+i]:
            return False
        t[j+i] = True
    return True

ans = 0
for p in perms:
    if valid_perm(p):
        ans += 1

print(ans)