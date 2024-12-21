from sys import *

d = [i.replace('\n', '') for i in stdin]
for i in range(len(d)):
    s = d[i]
    if s[0] != '#':
        if '#' in s:
            print(s[:s.find('#')])
        else:
            print(s)
