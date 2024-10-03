n = int(input())
last_hash = 0
err = 0
is_err = False
for i in range(n):
    block = int(input())
    current_hash = block % 256
    r = (block // 256) % 256
    m = block // 256 ** 2
    new_hash = (37 * (m + r + last_hash)) % 256
    if new_hash != current_hash or new_hash >= 100:
        if is_err is False:
            err = i
            is_err = True
    last_hash = current_hash
if is_err is False:
    print(-1)
else:
    print(err)
