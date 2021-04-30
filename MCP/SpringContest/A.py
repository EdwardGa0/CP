alph = input()
d = {}
for i in range(26):
    d[alph[i]] = chr(ord('a') + i)
m, k = map(int, input().split())
words = list(input().split())
words.sort(key=lambda w: [d[i] for i in w])
print(*words)