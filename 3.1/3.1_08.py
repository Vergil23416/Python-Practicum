n = int(input())
d = []
for i in range(n):
    d.append(input().split())
for i in range(n):
    c = 0
    item = d[i]
    if 'зайка' in item:
        c = item.index('зайка') + 1
        for j in range(item.index('зайка')):
            c += len(item[j])
        print(c)
    else:
        print('Заек нет =(')
