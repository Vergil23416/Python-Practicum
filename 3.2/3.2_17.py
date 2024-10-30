# добавить каждому в словарь, потом реплейсить тех кто есть
h = {}
d = []
j = set()
while True:
    s = input()
    if s == '':
        break
    s = s.split(' ')
    d.append(s)
for i in range(len(d)):
    s = d[i]
    j.add(s[0])
    j.add(s[1])
j = [i for i in j]
j.sort()
for i in range(len(j)):
    h[j[i]] = set()
for i in range(len(d)):
    s = d[i]
    for k in range(len(d)):
        n = d[k]
        if s[1] == n[0]:
            h[s[0]].add(n[1])
        elif s[1] == n[1]:
            h[s[0]].add(n[0])
    for k in range(len(d)):
        n = d[k]
        if s[0] == n[1]:
            h[s[1]].add(n[0])
        elif s[0] == n[0]:
            h[s[1]].add(n[1])
for i in range(len(d)):
    if d[i][1] in h[d[i][0]]:
        h[d[i][0]].remove(d[i][1])
    if d[i][0] in h[d[i][1]]:
        h[d[i][1]].remove(d[i][0])
    if d[i][0] in h[d[i][0]]:
        h[d[i][0]].remove(d[i][0])
    if d[i][1] in h[d[i][1]]:
        h[d[i][1]].remove(d[i][1])

for i in range(len(j)):
    print(f'{j[i]}: {", ".join(sorted(h[j[i]]))}')
