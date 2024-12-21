with open(input(), encoding='UTF-8') as input:
    n = [int(i) for i in input.read().split()]
k = len(n)
s = sum(n)
print(k)
print(len([i for i in n if i > 0]))
print(min(n))
print(max(n))
print(s)
print(f'{(s / k):.2f}')
