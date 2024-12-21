def can_eat(a, b):
    if (abs(a[0] * 2) == abs(b[0]) and abs(a[1] * 2) == abs(b[1])) or (
            abs(a[0]) == abs(b[0] * 2) and abs(a[1]) == abs(b[1] * 2)):
        return True
    else:
        return False
