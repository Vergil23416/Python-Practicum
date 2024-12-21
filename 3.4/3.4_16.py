from itertools import product, combinations

suits = ["бубен", "пик", "треф", "червей"]
s1, s2 = input(), input()
best_suit = [s for s in suits if s.startswith(s1[0:3])][0]
nominal = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
nominal.remove(s2)
comb = combinations(product(sorted(nominal), sorted(suits)), 3)
triads = [', '.join(' '.join(j) for j in sorted(i)) for i in comb if best_suit in ', '.join(' '.join(j) for j in i)]
for triad in triads[:10]:
    print(triad)
