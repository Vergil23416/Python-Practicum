a = int(input())
for i in range(1, a + 1):
    m = []
    for j in range(1, a + 1):
        m.append(i * j)
    print(*m)
