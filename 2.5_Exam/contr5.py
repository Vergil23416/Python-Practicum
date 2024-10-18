n = int(input())
d = []
for i in range(n):
    flag = True
    s = []
    while flag:
        f = input()
        if f == 'next':
            flag = False
            break
        s.append(int(f))
    d.append(round(sum(s) / len(s), 3))
print("{:.2f}".format(max(d)))
