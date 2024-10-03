d = []
a = int(input())

for i in range(a):
    name = input()
    n = int(input())
    d.append([name, sum(int(i) for i in str(n)), i])
d.sort(key=lambda x: x[1])
print(d[-1][0])
