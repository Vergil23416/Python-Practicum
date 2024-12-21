from sys import *
import json

n = input()
with open(n) as i:
    d = json.load(i)
s = stdin.readlines()
for i in s:
    if i != '':
        h = i.split('==')
        d[h[0].strip()] = h[1].strip()
with open(n, 'w') as hg:
    json.dump(d, hg, indent=4)
