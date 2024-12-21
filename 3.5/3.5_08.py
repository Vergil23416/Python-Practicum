with open(input(), encoding='UTF-8') as s:
    n1 = set([item for item in s.read().split()])
with open(input(), encoding='UTF-8') as s:
    n2 = set([item for item in s.read().split()])
ans = input()
a = n1 ^ n2
a = [i for i in a]
a.sort()
with open(ans, 'w', encoding='UTF-8') as s:
    print('\n'.join(a), file=s)
