ht = int(input())
wh = int(input())

c = len(str(wh * ht))

if ht > 0 and wh > 0:
    for row in range(ht):
        for cn in range(wh):
            if (row % 2) == 0:
                num = row * wh + cn + 1
            else:
                num = (row + 1) * wh - cn
            print(f'{num:>{c}}', end=' ')
        print()
