n = int(input())
digits = "abcdefghijklmnopqrstuvwxyz"
with open("public.txt", "r", encoding="UTF-8") as input_file:
    text = input_file.read()
new_text = [
    digits[(digits.index(char.lower()) + n) % len(digits)].upper() if char.isupper()
    else digits[(digits.index(char.lower()) + n) % len(digits)] if char.lower() in digits
    else char
    for char in text
]
with open("private.txt", "w") as output_file:
    output_file.write(''.join(new_text))
