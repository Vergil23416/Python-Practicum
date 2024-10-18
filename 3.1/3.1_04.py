d = []
while True:
    s = str(input())
    if s[-3:] != '@@@':
        if s[0:2] == '##':
            d.append(s[2:])
        else:
            d.append(s)
    if s == '':
        break

for i in range(len(d)):
    print(d[i], end='\n')
