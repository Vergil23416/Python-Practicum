from itertools import *

suits = sorted(["бубен", "пик", "треф", "червей"])
s1, s2, s3 = input(), input(), input()
best_suit = [s for s in suits if s.startswith(s1[0:3])][0]
nominal = sorted(["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"])
nominal.remove(s2)
comb = combinations(product(nominal, suits), 3)
triads = sorted([', '.join(' '.join(j) for j in sorted(i)) for i in comb if best_suit in ', '.join(' '.join(j) for j in i)])
for ind, triad in enumerate(triads):
    if triad == s3 and ind + 1 < len(triads):
        print(triads[ind + 1])
        break