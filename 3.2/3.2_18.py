d = {}
for _ in range(int(input())):
    s = input().split()
    z = f'{s[0][:-1]}-{s[1][:-1]}'
    if z not in d:
        d[z] = 1
    else:
        d[z] += 1
print(max(d.values()))
