def is_palindrome(a):
    if isinstance(a, int) or isinstance(a, float):
        a = str(abs(a))
    if a == a[::-1]:
        return True
    else:
        return False
