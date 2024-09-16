n, p, w, m = input(), int(input()), int(input()), int(input())
print(f'Чек\n{n} - {w}кг - {p}руб/кг\nИтого: {w * p}руб\nВнесено: {m}руб\nСдача: {m - (w * p)}руб')
