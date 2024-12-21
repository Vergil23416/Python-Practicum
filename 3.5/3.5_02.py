from sys import stdin

d = [i.split() for i in stdin]
c = len(d)
sum = 0
for i in range(len(d)):
    sum += (int(d[i][2]) - int(d[i][1]))
print(round(sum / c))
