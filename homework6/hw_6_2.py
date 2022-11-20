#1 9 3 4 -5 -15 -> min / max

def min_max(array: str) -> tuple:
    minimum = min(array.split())
    maximum = max(array.split())
    return int(minimum),int(maximum)

print (min_max("1 9 3 4 -5"))

#2 решение
def get_extremum(array: str) -> tuple:
    list_num = list(map(int, array.split()))
    return max(list_num), min(list_num)

print(get_extremum("1 5 6 -9 -80"))