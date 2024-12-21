from itertools import *

n = int(input())
d = [input().split(', ') for _ in range(n)]
d = [j for i in d for j in i]
d.sort()
for i in permutations(d, 3):
    print(' '.join(i))
