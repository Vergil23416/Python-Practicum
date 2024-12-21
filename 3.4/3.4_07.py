from itertools import *

d = [input() for _ in range(int(input()))]
for d1, d2 in list(combinations(d, 2)):
    print(f'{d1} - {d2}')
