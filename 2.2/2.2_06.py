p = int(input())
if p % 4 == 0:
    if p % 400 != 0 and p % 100 == 0:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
