with open("numbers.num", "rb") as input_file:
    data = input_file.read()
pairs_sum = 0
for i in range(0, len(data), 2):
    two_byte_number = int.from_bytes(data[i:i + 2], "big")
    pairs_sum += two_byte_number
checksum = pairs_sum % 2 ** 16
print(checksum)
