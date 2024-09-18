a, b, c = int(input()), int(input()), int(input())
if max(a, b, c) ** 2 == (min(a, b, c) ** 2 + ((a + b + c) - max(a, b, c) - min(a, b, c)) ** 2):
    print('100%')
elif max(a, b, c) ** 2 < (min(a, b, c) ** 2 + ((a + b + c) - max(a, b, c) - min(a, b, c)) ** 2):
    print('крайне мала')
else:
    print('велика')
