from itertools import *

c = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
name = ['пик', 'треф', 'бубен', 'червей']
name.remove(input())
for i, n in product(c, name):
    print(i, n)
