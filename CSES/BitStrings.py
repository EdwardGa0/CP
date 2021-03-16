ans = 1
for i in range(int(input())):
    ans = (ans*2)%int(1e9+7)
print(ans)