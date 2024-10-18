items = [str(input()) for _ in range(int(input()))]
flag = True
for i in range(len(items)):
    if items[i][0] not in 'авб':
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
