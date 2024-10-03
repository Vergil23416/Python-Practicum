p = 500
h = 250
print(p)

for _ in range(20):
    a = input()
    if a == 'Угадал!':
        break
    elif a == 'Меньше':
        p -= h
        print(p)
    elif a == 'Больше':
        p += h
        print(p)
    if h >= 2:
        h = (h + 1) // 2
