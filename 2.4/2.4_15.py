ht = int(input())
wh = int(input())

c = len(str(wh * ht))

for row in range(ht):
    for cn in range(wh):
        if cn % 2 == 0:
            num = cn * ht + row + 1
        else:
            num = (cn + 1) * ht - row
        print(f'{num:>{c}}', end=' ')
    print()
