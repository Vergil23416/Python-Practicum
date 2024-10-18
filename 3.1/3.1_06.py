items = [str(input()) for _ in range(int(input()))]
c = 0
for i in range(len(items)):
    c += items[i].count('зайка')
print(c)
