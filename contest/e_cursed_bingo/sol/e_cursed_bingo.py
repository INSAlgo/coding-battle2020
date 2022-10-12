import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

N, E = map(int, lines[0].split(' '))
Lab = [] # list containing a and b
for i in range(1, E + 1):
    a, b = map(int, lines[i].split(' '))
    Lab.append([a, b])

Ltest = [] # list of N 0s
for i in range(N):
    Ltest.append(0)
#we try to determine how many access have each room
for e in Lab:
    Ltest[e[0] - 1] += 1
    Ltest[e[1] - 1] += 1
#we choose the room that have the less access
print(min(Ltest))
