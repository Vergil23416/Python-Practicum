N, M = int(input()), int(input())
d = [input() for _ in range(N)]
flag = True
for i in range(M):
    d.append(input())
c = 0
j = []
for i in range(N + M):
    if d.count(d[i]) != 2:
        j.append(d[i])
        flag = False
if flag:
    print('Таких нет')
j.sort()
print('\n'.join(j))
