N = int(input())
d = [input() for _ in range(N)]
h = set()
for i in range(N):
    item = d[i].split()
    for j in range(len(item)):
        h.add(item[j])
print('\n'.join(h))
