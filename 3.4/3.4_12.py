n = int(input())
d = [input().split(', ') for _ in range(n)]
d = [i for j in d for i in j]
d.sort()
for i in range(len(d)):
    print(f'{i + 1}. {d[i]}')
