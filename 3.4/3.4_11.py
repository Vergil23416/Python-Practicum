from itertools import product

x = int(input())
y = int(input())
for i, j in product(range(1, x + 1), range(1, y + 1)):
    print(f'{((i - 1) * y + j):>{len(str(x * y))}}', end=' ')
    if j == y:
        print()
