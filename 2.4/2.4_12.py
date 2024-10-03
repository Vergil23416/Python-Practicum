ht = int(input())
wh = int(input())
c = len(str(wh * ht))
n = 1
for _ in range(ht):
    for _ in range(wh):
        print(f'{n:>{c}}', end=' ')
        n += 1
    print()
