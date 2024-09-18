p1, p2, p3 = int(input()), int(input()), int(input())
if max(p1, p2, p3) == p1 and min(p1, p2, p3) == p3:
    print('1. Петя\n2. Вася\n3. Толя')
elif max(p1, p2, p3) == p1 and min(p1, p2, p3) == p2:
    print('1. Петя\n2. Толя\n3. Вася')
elif max(p1, p2, p3) == p2 and min(p1, p2, p3) == p1:
    print('1. Вася\n2. Толя\n3. Петя')
elif max(p1, p2, p3) == p2 and min(p1, p2, p3) == p3:
    print('1. Вася\n2. Петя\n3. Толя')
elif max(p1, p2, p3) == p3 and min(p1, p2, p3) == p1:
    print('1. Толя\n2. Вася\n3. Петя')
else:
    print('1. Толя\n2. Петя\n3. Вася')
