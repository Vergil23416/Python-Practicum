from itertools import *

n = int(input())
d = [input() for _ in range(n)]
d.sort()
for i in permutations(d, 3):
    print(', '.join(i))
