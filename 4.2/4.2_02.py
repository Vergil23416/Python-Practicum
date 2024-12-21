def make_matrix(size, num=0):
    if isinstance(size, int):
        return [[num for _ in range(size)] for _ in range(size)]
    else:
        return [[num for _ in range(size[0])] for _ in range(size[1])]