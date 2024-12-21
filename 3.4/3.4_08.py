from itertools import *

d = [input() for _ in range(int(input()))]
n = int(input())
print('\n'.join(islice(cycle(d), n)))
