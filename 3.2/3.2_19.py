n = int(input())
d = []
for _ in range(n):
    s = input()
    s = s.split(': ')
    s = s[1]
    s = s.split(', ')
    h = set()

    for i in range(len(s)):
        h.add(s[i])
    h = [i for i in h]
    for i in range(len(h)):
        d.append(h[i])
d.sort()
for i in range(len(d)):
    if d.count(d[i]) == 1:
        print(d[i])
