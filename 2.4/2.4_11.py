def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


a = int(input())
count = 0
for _ in range(a):
    if p(int(input())):
        count += 1
print(count)
