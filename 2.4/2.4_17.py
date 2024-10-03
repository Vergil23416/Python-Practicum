n = int(input())
c = 0
for _ in range(n):
    num = int(input())
    origin = num
    revers = 0
    while num > 0:
        revers = revers * 10 + (num % 10)
        num //= 10
    if origin == revers:
        c += 1

print(c)
