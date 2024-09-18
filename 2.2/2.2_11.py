p = [int(x) for x in input()]
if min(p) + max(p) == (sum(p) - min(p) - max(p)) * 2:
    print('YES')
else:
    print('NO')
