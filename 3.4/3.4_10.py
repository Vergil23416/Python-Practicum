n = int(input())
print('А Б В')
for i in range(1, n - 1):
    for j in range(1, n - i):
        c = n - i - j
        print(i, j, c)
