n = int(input())
c = 0
wh = 1
maxl = 0

while c <= n:
    sl = 0
    for i in range(wh):
        c += 1
        if c <= n:
            sl += len(str(c))
        if i < wh - 1 and c < n:
            sl += 1

    if maxl < sl:
        maxl = sl

    wh += 1

c = 0
wh = 1

while c <= n:
    s = ''
    for i in range(wh):
        c += 1
        if c <= n:
            s += str(c)
        if i < wh - 1 and c < n:
            s += ' '
    wh += 1
    print(f'{s:^{maxl}}')
