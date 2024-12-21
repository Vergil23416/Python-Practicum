from itertools import *

n = int(input())
d = [input() for _ in range(n)]
d.sort()
for i in permutations(d, n):
    print(', '.join(i))
