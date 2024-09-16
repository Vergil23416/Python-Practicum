p1, p2 = list(map(int, input().zfill(3))), list(map(int, input().zfill(3)))
print(f'{(p1[0] + p2[0]) % 10}{(p1[1] + p2[1]) % 10}{(p1[2] + p2[2]) % 10}')
