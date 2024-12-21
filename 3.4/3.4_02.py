a1 = input().split(', ')
a2 = input().split(', ')
if len(a1) == len(a2):
    for i in range(len(a1)):
        print(f'{a1[i]} - {a2[i]}')
else:
    for i in range(min(len(a1), len(a2))):
        print(f'{a1[i]} - {a2[i]}')
