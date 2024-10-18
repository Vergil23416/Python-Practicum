d = [int(input()) for _ in range(int(input()))]
k = []
for i in range(len(d) - 1):
    if d[i + 1] < d[i]:
        k.append(d[i + 1])
print(max(k))
