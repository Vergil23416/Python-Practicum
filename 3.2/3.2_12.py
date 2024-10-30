d = [input() for _ in range(int(input()))]
h = {}
j = set()
for i in range(len(d)):
    if d.count(d[i]) != 1:
        h[d[i]] = d.count(d[i])
        j.add(d[i])
j = [i for i in j]
j.sort()
if len(j) != 0:
    for i in range(len(j)):
        print(f'{j[i]} - {h[j[i]]}')
else:
    print('Однофамильцев нет')
