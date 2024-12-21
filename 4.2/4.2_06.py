RECIPES = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1},
}

in_stock = {}


def order(*items):
    global in_stock

    for i in items:
        for ingrid in RECIPES[i]:
            if RECIPES[i].get(ingrid, 0) > in_stock[ingrid]:
                break
        else:
            for ingrid in RECIPES[i]:
                in_stock[ingrid] -= RECIPES[i][ingrid]
            return i

    if in_stock:
        return "К сожалению, не можем предложить Вам напиток"
