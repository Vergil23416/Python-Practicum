N = int(input())
d = [input() for _ in range(N)]

j = set()
for _ in range(int(input())):
    for _ in range(int(input())):
        j.add(input())
j = [i for i in j]
d.sort()
flag = True
for i in range(len(d)):
    if d[i] not in j:
        print(d[i])
        flag = False
if flag:
    print('Готовить нечего')
