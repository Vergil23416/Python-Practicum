a = input().split()
a = [float(i) for i in a]
while a[0] < a[1]:
    print(f'{a[0]:.2f}')
    a[0] += a[2]
