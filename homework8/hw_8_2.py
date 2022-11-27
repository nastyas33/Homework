def get_next_palindrome(value: int):
    value += 1
    while str(value) != str(value)[::-1]:
        value += 1
    return value
print(get_next_palindrome(55))