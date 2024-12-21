from sys import stdin
import json

with open('scoring.json') as f:
    d = json.load(f)
a = stdin.readlines()
s = 0
while d:
    t = d.pop(0)
    m = t['points'] // len(t['tests'])
    for x in t['tests']:
        if x['pattern'] == a.pop(0).strip():
            s += m
print(s)
