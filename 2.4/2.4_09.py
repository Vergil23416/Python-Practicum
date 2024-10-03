a = int(input())
w = ''
for _ in range(a):
    s = input()
    mx = max([int(i) for i in str(s)])
    w += str(mx)
print(w)
