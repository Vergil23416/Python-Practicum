p1, p2, p3 = int(input()), int(input()), int(input())
if max(p1, p2, p3) == p1:
    print('Петя')
elif max(p1, p2, p3) == p2:
    print('Вася')
else:
    print('Толя')
