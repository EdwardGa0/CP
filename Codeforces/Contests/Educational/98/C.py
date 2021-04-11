def ct(l, c):
    res = 0
    stack = 0
    for i in l:
        if i == c:
            stack += 1
        else:
            if stack > 0:
                stack -= 1
                res += 1
    return res

for _ in range(int(input())):
    s = input()
    rb = []
    sb = []
    for i in s:
        if i == '(' or i == ')':
            rb.append(i)
        else:
            sb.append(i)
    print(ct(rb, '(') + ct(sb, '['))
    
    