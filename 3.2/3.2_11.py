N = int(input())
d = [input() for _ in range(N)]
c = 0
for i in range(N):
    if d.count(d[i]) >= 2:
        c += 1
print(c)
