p = [int(x) for x in input() + input()]
print(str(max(p)) + str((sum(p) - max(p) - min(p)) % 10) + str(min(p)))

