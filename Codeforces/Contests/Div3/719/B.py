import sys
def cin():
    return sys.stdin.readline().strip('\n')

t = int(cin())
for _ in range(t):
    n = cin()
    ans = (len(n)-1)*9
    for i in range(1, 10):
        if int(str(i)*len(n)) <= int(n):
            ans += 1
        else:
            break
    sys.stdout.write(str(ans))