# Solution by Sebastien Goll

x = [int(i) for i in input().split()]
vm, vr, b = 0, 0, 0
for i in range(int(input())):
    s = input().split()

    if s[0] == 'b':
        b += int(s[1])

    else:
        if s[1] == 'm':
            vm += int(s[2])
        else:
            vr += int(s[2])

p = [0, 0, 0]
if vr >= x[0]:
    p[1] += x[0]
    x[0] = 0
else:
    p[1] += vr
    x[0] -= vr

if vm >= x[1]:
    p[1] += x[1]
    x[1] = 0
else:
    p[1] += vm
    x[1] -= vm

X = sum(x)

if b >= X:
    p[2] += X
    X = 0
else:
    p[2] += b
    X -= b

print(X, p[1], p[2])
