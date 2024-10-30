d = [int(i) for i in set(input().split('; '))]
d.sort()
for i in d:
    h = []
    for j in d:
        if i != j:
            a, b = i, j
            while b != 0:
                a, b = b, a % b
            if a == 1:
                h.append(str(j))
    if h:
        print(i, '-', ", ".join(h))
