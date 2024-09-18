p = input() + input() + input()
maxk = []
for i in '0123456789':
    maxk.append([p.count(i), i])
print(max(maxk)[1])
