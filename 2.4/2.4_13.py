ht = int(input())
wh = int(input())
c = len(str(ht * wh))
for i in range(1, ht + 1):
    for j in range(i, i + ht * (wh - 1) + 1, ht):
        print(f'{j:>{c}}', end=' ')
        if j == i + ht * (wh - 1):
            print()
