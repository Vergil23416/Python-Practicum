def sumBase(n, base):
    total = 0
    while n > 0:
        total += n % base
        n //= base
    return total


n = int(input())
maxs = 0
base = 0
for i in range(2, 11):
    if sumBase(n, i) > maxs:
        maxs = sumBase(n, i)
        base = i
print(base)
