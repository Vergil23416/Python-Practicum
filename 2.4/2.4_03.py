p = int(input())
n = 0
c = 1

for i in range(1, p + 1):
    if n != c:
        print(f'{i}', end=(' '))
        n += 1
    else:
        print(f'\n{i}', end=(' '))
        n = 1
        c += 1
