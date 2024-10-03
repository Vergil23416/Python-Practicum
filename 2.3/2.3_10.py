x, y = 0, 0
while True:
    a = input()
    if a == 'СЕВЕР':
        b = int(input())
        y += b
    elif a == 'ВОСТОК':
        b = int(input())
        x += b
    elif a == 'ЗАПАД':
        b = int(input())
        x -= b
    elif a == 'ЮГ':
        b = int(input())
        y -= b
    elif a == 'СТОП':
        print(y)
        print(x)
        break
