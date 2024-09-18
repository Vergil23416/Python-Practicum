p1, p2, p3 = int(input()), int(input()), int(input())
if p1 + p2 > p3 and p2 + p3 > p1 and p1 + p3 > p2:
    print('YES')
else:
    print('NO')
