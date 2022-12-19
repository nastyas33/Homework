def alphabet(text: str):
    alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for word in text.lower():
        if word in alphabet_en:
            result.append(alphabet_en.index(word)+1)
    return result

print(alphabet("The sunset sets at twelve o' clock"))

#2решение
import string
from functools import reduce

def get_numbers(array: str) -> str:
    indexes = [string.ascii_lowercase.index(char.lower()) + 1 for char in array
               if char.lower() in string.ascii_lowercase]
    res = reduce(lambda  x, y: f"{x} {y}", indexes)
    return res

print(get_numbers("The sunset is at about 8 o'clock"))