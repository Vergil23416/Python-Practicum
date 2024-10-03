def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


p1, p2 = [int(input()) for _ in range(2)]

print(gcd(p1, p2))
