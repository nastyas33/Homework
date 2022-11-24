def get_digit(word: str) -> int or None:
    for symbol in word:
        if symbol.isdigit():
            return int(symbol)
    return None


def order(array: str) -> str:
    return ' '.join(sorted(array.split(), key=get_digit))


print(order("k5ll i9bh a2ll"))