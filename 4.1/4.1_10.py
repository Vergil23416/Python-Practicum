def merge(a, b):
    d = a + b
    d = [int(i) for i in d]
    d.sort()
    return tuple(d)
