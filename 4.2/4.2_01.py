def make_list(a, b=0):
    if b == '':
        return list(0 for _ in range(a))
    else:
        return list(b for _ in range(a))
