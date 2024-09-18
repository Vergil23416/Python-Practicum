s = [input(), input(), input()]
s.sort()
for i in s:
    if "зайка" in i:
        print(i, len(i))
        break
