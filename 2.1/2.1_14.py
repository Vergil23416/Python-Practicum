p1, p2, p3 = int(input()), int(input()), int(input())
print(f'{str((p1 + ((p3 + p2) // 60)) % 24).zfill(2)}:{str(((p2 + p3) % 60)).zfill(2)}')
