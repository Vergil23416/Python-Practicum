s = int(input())
c = int(input())

st = s * c + (s - 1)

for row in range(s):
    for cn in range(s):
        print(f'{((row + 1) * (cn + 1)): ^{c}}', end='')
        if cn == s - 1:
            print()
        else:
            print('|', end='')
    if row + 1 != s:
        print('-' * st)