p1, p2 = [int(input()) for _ in range(2)]
lis = []
if p2 >= p1:
    for i in range(p1, p2 + 1):
        lis.append(i)
else:
    for i in range(p2, p1 + 1):
        lis.append(i)
    lis.reverse()
print(*lis)
