fn = input()
with open(fn, 'rb') as f:
    sz = len(f.read())
sc = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
w = 0
while sz > 1024 and w < len(sc):
    w += 1
    sz, r = divmod(sz, 1024)
    sz += r > 0
print(f'{sz}{sc[w]}')
