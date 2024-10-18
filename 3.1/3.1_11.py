n = int(input())
d = [input() for _ in range(n)]
s = input()
for i in range(n):
    if s.lower() in d[i].lower():
        print(d[i])
