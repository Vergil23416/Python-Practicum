while True:
    s = input()
    if s != '':
        if s[0] != '#':
            if '#' in s:
                print(s[:s.find('#')])
            else:
                print(s)
    else:
        break
