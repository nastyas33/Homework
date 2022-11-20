def sum_range(start: int, end: int) -> int:
    counter = 0
    if start > end:
        start, end = end, start
    for number in range(start, end + 1):
        counter += number
    return counter

print (sum_range(start=9, end=4))