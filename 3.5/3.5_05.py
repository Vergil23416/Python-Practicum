from sys import *

d = set(i for j in stdin for i in j.replace('\n', '').split())
d = [i for i in d]
d.sort()
for i in range(len(d)):
    if d[i].lower() == d[i][::-1].lower():
        print(d[i])
