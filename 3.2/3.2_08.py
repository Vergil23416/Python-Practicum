d = {}
for _ in range(int(input())):
    string = input()
    i, *j = string.split()
    d[i] = j
eat = input()
h = []
for i in d:
    if eat in d[i]:
        h.append(i)
if h:
    h.sort()
    for i in h:
        print(i)
else:
    print('Таких нет')
