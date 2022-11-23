import random

def random__numbers (n1: int, amount: int) ->int:
    from random import sample
    lst = random.sample(range(n1), amount)
    from collections import Counter
    count = Counter(lst)
    return count

print(random__numbers(1000, 15))

#второйспособ количество повторений
from random import randint
def random_list(start: int, end:int, count2: int) -> list:
    random_list = []
    for _ in range(count2):
        random_list.append(randint(start, end))
    return random_list

def count_same(n: list) -> int:
    counter1 = 0
    for num in set(n):
        if n.count(num) > 1:
            counter1 += 1
    return counter1

print(count_same(random_list(start=1, end=20, count2=15)))