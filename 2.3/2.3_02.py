count = 0
while True:
    a = input()
    if 'зайка' in a:
        count += 1
    if a == 'Приехали!':
        print(count)
        break
