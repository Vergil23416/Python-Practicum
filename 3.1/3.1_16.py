L = int(input())
items = [input() for _ in range(int(input()))]
for i in items:
    if L > 3:
        if len(i) >= L - 3:
            i = i[:L - 3] + "..."
        else:
            if L == 4:
                i = i + "..."
        L -= len(i)
        print(i)
