d, k = [], set()
for _ in range(int(input())):
    d.append(input())
for _ in range(int(input())):
    s = input()
    k.add(s)
    for i in range(int(input())):
        if input() not in d:
            k.discard(s)
if k:
    for i in sorted(k):
        print(i)
else:
    print('Готовить нечего')
