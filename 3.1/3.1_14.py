s = input().split()
P = int(input())
d = [str(int(i) ** P) for i in s]
print(' '.join(d))
