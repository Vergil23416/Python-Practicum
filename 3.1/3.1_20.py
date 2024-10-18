from math import *

d = input().split()
flag = True
while flag:
    d = [i for i in d if i != 'k']
    if len(d) == 1:
        print(d[0])
        flag = False
        break
    if len(d) == 2:
        if str(d[1]) == '~' and str(d[0]) not in '+-/*@~!#':
            g = int(d[0]) * (-1)
            d[0] = g
            d.remove(d[1])
        elif str(d[1]) == '!' and str(d[0]) not in '+-/*@~!#':
            g = factorial(int(d[0]))
            d[0] = g
            d.remove(d[1])

    if len(d) == 3:
        if str(d[1]) == '~' and str(d[0]) not in '+-/*@~!#':
            g = int(d[0]) * (-1)
            d[1] = g
            d.remove(d[0])
        elif str(d[1]) == '!' and str(d[0]) not in '+-/*@~!#':
            g = factorial(int(d[0]))
            d[1] = g
            d.remove(d[0])
        elif str(d[1]) == '#' and str(d[0]) not in '+-/*@~!#':
            g = int(d[0])
            d[1] = g
        if str(d[2]) in '+-/*' and str(d[1]) not in '+-/*@~!#':
            if str(d[2]) == '+':
                g = int(d[0]) + int(d[1])
            elif str(d[2]) == '*':
                g = int(d[0]) * int(d[1])
            elif str(d[2]) == '-':
                g = int(d[0]) - int(d[1])
            elif str(d[2]) == '/':
                g = int(d[0]) // int(d[1])
            d[2] = g
            d.remove(d[0])
            d.remove(d[0])
    for i in range(len(d) - 3):
        if str(d[i + 1]) in '~!#' and str(d[i]) not in '+-/*@~!#':
            if str(d[i + 1]) == '~':
                g = int(d[i]) * (-1)
                d[i + 1] = g
                d[i] = 'k'
                break
            elif str(d[i + 1]) == '!':
                g = factorial(int(d[i]))
                d[i + 1] = g
                d[i] = 'k'
                break
            elif str(d[i + 1]) == '#':
                g = int(d[i])
                d[i + 1] = g
                break
        if str(d[i + 2]) in '+-*/' and str(d[i + 1]) not in '+-/*@~!#' and str(d[i]) not in '+-/*@~!#':
            if str(d[i + 2]) == '+':
                g = int(d[i]) + int(d[i + 1])
            elif str(d[i + 2]) == '*':
                g = int(d[i]) * int(d[i + 1])
            elif str(d[i + 2]) == '-':
                g = int(d[i]) - int(d[i + 1])
            elif str(d[i + 2]) == '/':
                g = int(d[i]) // int(d[i + 1])
            d[i + 2] = g
            d[i] = 'k'
            d[i + 1] = 'k'
            break
        if str(d[i + 2]) in '~!#' and str(d[i + 1]) not in '+-/*@~!#':
            if str(d[i + 2]) == '~':
                g = int(d[i + 1]) * (-1)
                d[i + 2] = g
                d[i + 1] = 'k'
                break
            elif str(d[i + 2]) == '!':
                g = factorial(int(d[i + 1]))
                d[i + 2] = g
                d[i + 1] = 'k'
                break
            elif str(d[i + 2]) == '#':
                g = int(d[i + 1])
                d[i + 2] = g
                break
        if str(d[i + 3]) in '+-*/' and str(d[i + 2]) not in '+-/*@~!#' and str(d[i + 1]) not in '+-/*@~!#':
            if str(d[i + 3]) == '+':
                g = int(d[i + 1]) + int(d[i + 2])
            elif str(d[i + 3]) == '*':
                g = int(d[i + 1]) * int(d[i + 2])
            elif str(d[i + 3]) == '-':
                g = int(d[i + 1]) - int(d[i + 2])
            elif str(d[i + 3]) == '/':
                g = int(d[i + 1]) // int(d[i + 2])
            d[i + 3] = g
            d[i + 1] = 'k'
            d[i + 2] = 'k'
            break
        if str(d[i + 3]) in '~!#' and str(d[i + 2]) not in '+-/*@~!#':
            if str(d[i + 3]) == '~':
                g = int(d[i + 2]) * (-1)
                d[i + 3] = g
                d[i + 2] = 'k'
                break
            elif str(d[i + 3]) == '!':
                g = factorial(int(d[i + 2]))
                d[i + 3] = g
                d[i + 2] = 'k'
                break
            elif str(d[i + 3]) == '#':
                g = int(d[i + 2])
                d[i + 3] = g
                break
        if str(d[i + 3]) == '@' and str(d[i]) not in '+-/*@~!#' and str(d[i + 1]) not in '+-/*@~!#' and str(
                d[i + 2]) not in '+-/*@~!#':
            d[i], d[i + 1], d[i + 2] = d[i + 1], d[i + 2], d[i]
            d[i + 3] = 'k'
            break
