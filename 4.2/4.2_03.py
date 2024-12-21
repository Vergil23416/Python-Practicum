def gcd(*args):
    d = list(args)
    n = d[0]
    for i in d[1:]:
        if n < i:
            s = n
            s, n, i = n, i, s
        while i != 0:
            s = i
            s, i, n = i, n % i, s
    return n
