d = set()


def modern_print(s):
    if s not in d:
        d.add(s)
        return print(s)
