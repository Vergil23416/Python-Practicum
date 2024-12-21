from itertools import product

s = input()
print('a b c f')
for a, b, c in product([0, 1], repeat=3):
    print(a, b, c, int(eval(s, {'a': a, 'b': b, 'c': c})))
