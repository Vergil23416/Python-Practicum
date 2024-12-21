with open('transliteration.txt', 'w', encoding='UTF-8') as output:
    with open('cyrillic.txt', encoding='UTF-8') as inp:
        digits = {
            'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
            'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
            'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
            'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch',
            'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia', 'Ь': '', 'Ъ': ''
        }
        for line in inp:
            for char in line:
                current = char.upper()
                if current in digits:
                    if char.isupper():
                        char = digits[current]
                    else:
                        char = digits[current].lower()
                else:
                    char = char
                print(char, end='', file=output)
