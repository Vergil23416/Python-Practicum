with open("secret.txt", 'r', encoding='UTF-8') as s:
    print(''.join(chr(ord(c) % 128) for c in s.read()))