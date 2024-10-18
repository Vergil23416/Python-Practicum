items = []
d = []
while (s := input()) != 'ФИНИШ':
    items.extend(s.lower().split())
maxc = 0
items = ''.join(items)
for i in set(items):
    maxc = max(maxc, items.count(i))
for i in set(items):
    if items.count(i) == maxc:
        d.append(i)
print(min(d))
