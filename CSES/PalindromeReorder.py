s = input()
freq = [0] * 26

def to_val(c):
    return ord(c) - ord('A')

def to_c(i):
    return chr(i + ord('A'))

for c in s:
    freq[to_val(c)] += 1

def can_pal():
    mid = 0
    for i in range(0, 26):
        if freq[i] & 1:
            mid += 1
    return mid <= 1

if can_pal():
    ans = []
    mid = ''
    for i in range(0, 26):
        if freq[i] & 1:
            mid = to_c(i) * freq[i]
        else:
            ans.append(to_c(i) * (freq[i]//2))
    print(''.join(ans) + mid + ''.join(reversed(ans)))
else:
    print("NO SOLUTION")