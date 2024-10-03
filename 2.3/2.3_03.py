p1, p2 = [int(input()) for _ in range(2)]
lis = []
for i in range(p1, p2 + 1):
    lis.append(i)
print(*lis)
