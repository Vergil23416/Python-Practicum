d = input().split()
flag = True
while flag:
    if len(d) == 1:
        print(d[0])
        flag = False
        break
    for i in range(len(d) - 2):
        if str(d[i + 2]) in '+-*':
            if str(d[i + 2]) == '+':
                g = int(d[i]) + int(d[i + 1])
            elif str(d[i + 2]) == '*':
                g = int(d[i]) * int(d[i + 1])
            elif str(d[i + 2]) == '-':
                g = int(d[i]) - int(d[i + 1])
            d[i + 2] = g
            d.remove(d[i])
            d.remove(d[i])
            break
