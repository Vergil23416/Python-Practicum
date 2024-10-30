def convert_to(number, base):
    digits = '0123456789abcdef'
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result


a = input().split()
d = []
print('[')
for i in range(len(a)):
    j = convert_to(int(a[i]), 2)
    d.append({"digits": len(j),
              "units": j.count('1'),
              "zeros": j.count('0')})
for i in range(len(d)):
    print(d[i], end=',\n')
print(']')
