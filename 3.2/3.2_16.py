h = set()
d = []
while True:
    s = input()
    if s == '':
        break
    d = s.split(' ')
    if 'зайка' in s:
        for i in range(len(d)):
            if i == 0:
                if d[i] == 'зайка':
                    h.add(d[i + 1])
            if i == len(d) - 1:
                if d[i] == 'зайка':
                    h.add(d[i - 1])
            if 0 < i < len(d) - 1:
                if d[i] == 'зайка':
                    h.add(d[i - 1])
                    h.add(d[i + 1])
h = [i for i in h]
for i in h:
    print(i)
