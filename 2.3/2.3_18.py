p = int(input())
lis = []
while p != 1:
    for i in range(2, int(p) + 1):
        if p % i == 0:
            p /= i
            lis.append(str(i))
            break
print(' * '.join(lis))
