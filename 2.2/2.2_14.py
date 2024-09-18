p = [int(x) for x in input()]
k = str(max(p)) + str(sum(p) - min(p) - max(p))
if min(p) == 0:
    s = str(sum(p) - max(p)) + '0'
else:
    s = str(min(p)) + str(sum(p) - min(p) - max(p))
print(s, k)
