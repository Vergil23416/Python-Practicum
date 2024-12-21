nums = []
odds, evens = [], []


def enter_results(*items):
    global nums, odds, evens
    nums += items
    odds, evens = nums[::2], nums[1::2]


def get_sum():
    return round(sum(odds), 2), round(sum(evens), 2)


def get_average():
    return round(sum(odds) / len(odds), 2), round(sum(evens) / len(evens), 2)
