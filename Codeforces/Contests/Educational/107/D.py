def itoc(i):
    return chr(ord('a') + i)

n, k = map(int, input().split())
seq = []
for i in range(k):
    seq.append(itoc(i))
    for j in range(i+1, k):
        seq.append(itoc(i))
        seq.append(itoc(j))

while len(seq) < n:
    seq += seq
print(''.join(seq)[:n])