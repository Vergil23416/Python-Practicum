p1, p2, p3, p4 = int(input()), int(input()), int(input()), int(input())
NM = p1 * p2
for i in range(1, p1 + 1):
    if (i * p3) + ((p1 - i) * p4) == NM:
        print(i, p1 - i)

