#вывод длины самого короткого слова
def min_len (str1: str) -> int:
    return min(map(len, str1.split()))

print(min_len("London is the capital of Great Britain"))

#2 решение
def get_shortes (array: str) -> int:
    return len(min(array.split(),key=len))

print(get_shortes("Hello aold, we have beatiful news"))