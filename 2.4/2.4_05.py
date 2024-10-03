a = int(input())
i = 0
count = 0
flag = False
while i < a:
    b = input()
    if b == 'зайка' and not flag:
        count += 1
        flag = True
    if b == 'ВСЁ':
        i += 1
        flag = False
print(count)
