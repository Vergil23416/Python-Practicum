N, M = int(input()), int(input())
d = [input() for _ in range(N)]
for i in range(M):
    d.append(input())
c = 0
for i in range(N + M):
    if d.count(d[i]) != 2:
        c += 1
if c == 0:
    print('Таких нет')
else:
    print(c)
