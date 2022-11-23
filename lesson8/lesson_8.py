#1
#array_diff ([1,2,2,2,3], [2]) == [1,3]
def array_diff(a, b):
    result = [number for number in a if number not in b]
    return result

#42156 --> max 65421

#2d 1option
def spin_words(sentence):
    split_sentence = sentence.split()
    result = []
    for word in split_sentence:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)

    return " ".join(result)

#2d 2option

def spin_words_2(sentence: str):
    result = [word[::-1] if len(word) >= 5 else word for word in sentence.split()]
    return " ".join(result)

#3task
def find_it(seq):
    result = list(filter(lambda x: seq.count(x) % 2 != 0, seq))
    return result[0]

#4task
from math import sqrt
def is_square(n):
    return True if sqrt(n) == int(sqrt(n)) else False

#5task
def descending_order(num: int) -> int:
    #lst_num = list(str(num))
    int_lst_num = list(map(int, str(num)))
    int_lst_num.sort(reverse=True)
    str_lst_num = map(str, int_lst_num)
    return int("".join(str_lst_num))

print(descending_order(12356))

# [1, 0, 1, 2, 0, 1, 3] -> return [1, 1, 2, 1, 3, 0, 0]
def move_zeroes(lst: list):
    result = [num for num in lst if num != 0] #[1, 1, 2, 1, 3]
    delta = len(lst) - len(result)
    for _ in range(1, delta + 1):
        result.append(0)
    return result

print(move_zeroes([1, 0, 1, 2, 0, 1, 3]))

#1645 -> 1+6+4+5 -> 1+6 -> 7
from functools import reduce
def digital_root(n):
    return n if n <= 9 else digital_root(reduce(lambda x, y: int(x) + int(y), str(n)))

print(digital_root(1645))