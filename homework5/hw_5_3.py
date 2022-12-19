def isogram (word: str):
    for letter in word:
        if word.count(letter) > 1:
            return (word, False)
    return (word, True)

print(isogram("Hello"))

#2 решение
def is_isogram(array: str):
    if len(array.lower()) == len("".join(set(array.lower()))): #set убирает все одинаковые
        return True
    else:
        return False

print(is_isogram("Hello"))