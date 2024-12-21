from sys import *

d = [i.replace('\n', '') for i in stdin]
for i in range(len(d) - 1):
    if d[-1].lower() in d[i].lower():
        print(d[i])
