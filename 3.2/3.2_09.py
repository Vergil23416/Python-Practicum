h = []
while True:
    s = input()
    if s == '':
        break
    else:
        h.append(s)
d = set()
k = ' '.join(h)
k = k.split()
for i in range(len(h)):
    item = h[i].split()
    for j in range(len(item)):
        d.add(item[j])
d = [i for i in d]
for i in range(len(d)):
    print(d[i], k.count(d[i]))
