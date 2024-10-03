from math import *

n = int(input())
print(gcd(*[int(input()) for _ in range(n)]))
