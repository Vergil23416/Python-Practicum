count = 0
while True:
    a = float(input())
    if a >= 500:
        count += a * 0.9
    elif 0 < a < 500:
        count += a
    if a == 0:
        print(round(count, 1))
        break
