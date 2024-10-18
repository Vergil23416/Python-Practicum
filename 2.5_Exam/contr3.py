a, b = int(input()), int(input())
d = []
for i in range(b, a + 1, ((b - a) % 10)):
    d.append(str(i))
print(', '.join(d))
