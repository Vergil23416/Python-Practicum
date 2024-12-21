a, b = input(), input()
d = []
with open(a, 'r') as i:
    for j in i:
        d.append(j.replace('\t', '').strip().split())
d = [i for i in d if len(i) != 0]
with open(b, 'w') as i:
    for j in d:
        print(' '.join(j), file=i)
