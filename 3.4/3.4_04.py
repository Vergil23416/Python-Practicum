from itertools import *

a = input().replace(' ', ' $')
a = a.split('$')
for value in accumulate(a):
    print(value)
