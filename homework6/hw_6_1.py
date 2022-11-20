#1 решение
def simple_numbers (array: int):
    if array < 2:
        return False
    for number in range(2, array +1):
        if array % number == 0:
            return False
        else:
            return True

print(simple_numbers(11))

#2 решение

def is_prime(n):
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n #оператор сравнения так же возвращает либо True либо False

print(is_prime(119))
