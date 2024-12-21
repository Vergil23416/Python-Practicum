from sys import stdin

d = [i.replace('\n', '').split() for i in stdin]
d = [int(j) for i in d for j in i]
print(sum(d))
