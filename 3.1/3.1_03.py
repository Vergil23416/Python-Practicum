n = int(input())
c = int(input())
for i in range(c):
    s = input()
    if len(s) > n:
        print(f'{s[:n - 3]}...')
    else:
        print(s)
