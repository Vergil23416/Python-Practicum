p = str(input())
print(f'{max(int(p[2]) + int(p[1]), int(p[0]) + int(p[1]))}{min(int(p[0]) + int(p[1]), int(p[2]) + int(p[1]))}')
