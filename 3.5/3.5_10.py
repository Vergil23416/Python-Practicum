with open(input()) as i:
    d = [j for j in i.read().split('\n') if j != '']
print('\n'.join(d[-(int(input())):]))
