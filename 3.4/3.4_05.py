a1 = input().split(', ')
a2 = input().split(', ')
a3 = input().split(', ')
d = []
for i in range(len(a1)):
    d.append(a1[i])
for i in range(len(a2)):
    d.append(a2[i])
for i in range(len(a3)):
    d.append(a3[i])
d.sort()
for i in range(len(d)):
    print(f'{i + 1}. {d[i]}')
