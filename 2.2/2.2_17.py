from math import sqrt

a, b, c = float(input()), float(input()), float(input())

if a == 0 and c == 0 and b == 0:
    print('Infinite solutions')
elif a == 0 and b == 0:
    print('No solution')
elif a == 0:
    x = -c / b
    print(round(x, 2))
elif b ** 2 - (4 * a * c) > 0:
    x1 = ((-b + sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    x2 = ((-b - sqrt(b ** 2 - (4 * a * c)))) / (2 * a)
    print(round(min(x1, x2), 2), round(max(x1, x2), 2))
elif b ** 2 - (4 * a * c) == 0:
    print(round(-b / (2 * a), 2))
else:
    print('No solution')
