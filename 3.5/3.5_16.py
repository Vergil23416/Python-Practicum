from sys import stdin

q, *fns = [s.strip() for s in stdin]
f = False
for fn in fns:
    with open(fn, encoding='UTF-8') as fh:
        d = ' '.join(fh.read().lower().split())
        if q.lower() in d:
            print(fn)
            f = True
if not f:
    print('404. Not Found')
